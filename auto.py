import add_json
import generate

category = 'バトル'
button_name = '戦争すっか？'
add_json.update_json_data(category, button_name)
generate.generate()