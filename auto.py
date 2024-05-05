import add_json
import generate

category = 'ＩＱ３'
button_name = '蛙が先か鶏が先か'
add_json.update_json_data(category, button_name)
generate.generate()