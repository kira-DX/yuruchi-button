import add_json
import generate

category = 'くしゃみ'
button_name = 'くしゃみでた'
add_json.update_json_data(category, button_name)
generate.generate()