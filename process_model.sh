conda activate tensorflowlite

python xml_to_csv.py

python change_number_labels.py --file_label_name /conf_model/labelmap.pbtxt --file_conf_model /conf_model/model_conf.config

python generate_tfrecord.py --csv_input=train_labels.csv --label_input conf_model/labelmap.pbtxt --image_dir=train --output_path=datatfrecord/train.record

python generate_tfrecord.py --csv_input=test_labels.csv --label_input conf_model/labelmap.pbtxt --image_dir=test --output_path=datatfrecord/test.record

python train.py --logtostderr --train_dir=conf_model/ --pipeline_config_path=conf_model/model_conf.config




