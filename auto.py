import add_json
import generate

category = 'その他'
button_name = '助けて！'
add_json.update_json_data(category, button_name)
generate.generate()