import add_json
import generate

category = 'モノマネ'
button_name = 'ドラムロール'
add_json.update_json_data(category, button_name)
generate.generate()