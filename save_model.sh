conda activate tensorflowlite

var=()
for filename in conf_model/*.meta; do
    var+=("$filename")
done


var=($(for each in ${var[@]}; do echo $each; done | sort -rn))
new_var="${var[0]}"
new_var="${new_var/.meta/}"

echo "$new_var"
mkdir tflite
python export_tflite_ssd_graph.py --pipeline_config_path conf_model/model_conf.config --trained_checkpoint_prefix "$new_var" --output_directory tflite --max_detections 25

tflite_convert \
--output_file=tflite/model.tflite \
--graph_def_file=tflite/tflite_graph.pb \
--input_arrays=normalized_input_image_tensor \
--output_arrays='TFLite_Detection_PostProcess','TFLite_Detection_PostProcess:1','TFLite_Detection_PostProcess:2','TFLite_Detection_PostProcess:3' \
--input_shape=1,300,300,3 \
--allow_custom_ops
