import com.vader.sentiment.analyzer.SentimentPolarities;
import org.apache.flink.api.common.eventtime.WatermarkStrategy;
import org.apache.flink.api.common.functions.MapFunction;
import org.apache.flink.api.common.typeinfo.BasicTypeInfo;
import org.apache.flink.api.common.typeinfo.TypeInformation;
import org.apache.flink.connector.mongodb.source.MongoSource;
import org.apache.flink.connector.mongodb.source.reader.deserializer.MongoDeserializationSchema;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.bson.BsonDocument;
import com.vader.sentiment.analyzer.SentimentAnalyzer;
import org.bson.BsonInvalidOperationException;
import org.bson.BsonString;


public class FlinkLower {
    public static void main(String[] args) throws Exception {

        MongoSource<String> source = MongoSource.<String>builder()
                .setUri("mongodb://127.0.0.1:27017")
                .setDatabase("socialMediaData")
                .setCollection("newsCollection")
                .setDeserializationSchema(new MongoDeserializationSchema<String>() {
                    @Override
                    public String deserialize(BsonDocument document) {
                        try{
                            BsonString description = document.getString("description");
                            return description.toString();
                        }catch (BsonInvalidOperationException e){
                            return "";
                        }
                    }

                    @Override
                    public TypeInformation<String> getProducedType() {
                        return BasicTypeInfo.STRING_TYPE_INFO;
                    }
                })
                .build();

        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        DataStream<String> descriptionStream = env.fromSource(source, WatermarkStrategy.noWatermarks(), "MongoDB-Source");
        DataStream<String> sentimentStream = descriptionStream.map(
                (MapFunction<String, String>) value -> SentimentAnalyzer.getScoresFor(value).toString());

        sentimentStream.print().setParallelism(1);

        env.execute("MongoDB Sentiment Analysis");

    }
}
