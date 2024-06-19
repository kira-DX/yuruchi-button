import add_json
import generate

category = '名言'
button_name = 'すいません…勝てそうです'
add_json.update_json_data(category, button_name)
generate.generate()