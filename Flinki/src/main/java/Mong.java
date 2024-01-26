import java.net.Inet4Address;
import org.apache.flink.api.common.eventtime.WatermarkStrategy;
import org.apache.flink.api.common.typeinfo.BasicTypeInfo;
import org.apache.flink.api.common.typeinfo.TypeInformation;
import org.apache.flink.connector.mongodb.source.MongoSource;
import org.apache.flink.connector.mongodb.source.reader.deserializer.MongoDeserializationSchema;
import org.apache.flink.configuration.MemorySize;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.bson.BsonDocument;

public class FlinkMongoDbJob {
    public static void main(String[] args) {
        try {

            MongoSource<String> source = MongoSource.<String>builder()
                    .setUri("mongodb://127.0.0.1:27017")
                    .setDatabase("my_db")
                    .setCollection("my_coll")
                    .setProjectedFields("_id", "f0", "f1")
                    .setFetchSize(2048)
                    .setLimit(10000)
                    .setNoCursorTimeout(true)
                    .setPartitionSize(MemorySize.ofMebiBytes(64))
                    .setSamplesPerPartition(10)
                    .setDeserializationSchema(new MongoDeserializationSchema<String>() {
                        @Override
                        public String deserialize(BsonDocument document) {
                            return document.toJson();
                        }

                        @Override
                        public TypeInformation<String> getProducedType() {
                            return BasicTypeInfo.STRING_TYPE_INFO;
                        }
                    })
                    .build();

            StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

            env.fromSource(source, WatermarkStrategy.noWatermarks(), "MongoDB-Source")
                    .setParallelism(2)
                    .print()
                    .setParallelism(1);

            env.execute("Flink MongoDB Job");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
