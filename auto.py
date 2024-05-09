import add_json
import generate

category = 'ＩＱ３'
button_name = '天気予報'
add_json.update_json_data(category, button_name)
generate.generate()