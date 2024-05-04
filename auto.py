import add_json
import generate

category = '名言'
button_name = '昨日も綺麗だったよ、ゆるちは。'
add_json.update_json_data(category, button_name)
generate.generate()