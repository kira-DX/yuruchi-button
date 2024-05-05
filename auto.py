import add_json
import generate

category = 'その他'
button_name = 'なんで？（イケボ）'
add_json.update_json_data(category, button_name)
generate.generate()