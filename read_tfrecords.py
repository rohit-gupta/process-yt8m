import tensorflow as tf 
import numpy as np
from glob import glob

data_dir = "/home/c3-0/rohitg/datasets/yt8m/shards/"

tfrecords = glob(data_dir + "validate*.tfrecord")

output = open("yt8m_1percent_validate.txt", "w")
# log = open("tf_recordparsing.log", "w")

for tfrecord in tfrecords:
    raw_dataset = tf.data.TFRecordDataset(tfrecord)

    count = 0

    for raw_record in raw_dataset.take(100000):
        example = tf.train.Example()
        example.ParseFromString(raw_record.numpy())
        
        result = {}
        # example.features.feature is the dictionary
        for key, feature in example.features.feature.items():

        # The values are the Feature objects which contain a `kind` which contains:
        # one of three fields: bytes_list, float_list, int64_list

            if key in ["id", "labels"]:
                kind = feature.WhichOneof('kind')
                result[key] = np.array(getattr(feature, kind).value)

        count += 1
        
        print(",".join([result["id"][0].decode("utf-8")] + [str(label) for label in result["labels"]]), file=output)

    print("Read", count, "videos from shard", tfrecord)

# log.close()
output.close()
