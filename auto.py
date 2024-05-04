import add_json
import generate

category = '煽り'
button_name = '何が悪いんですか！'
add_json.update_json_data(category, button_name)
generate.generate()