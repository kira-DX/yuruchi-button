import add_json
import generate

category = '名言'
button_name = '夜にやりがちゆるち'
add_json.update_json_data(category, button_name)
generate.generate()