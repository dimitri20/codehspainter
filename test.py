


with open("download.jpg.csv", 'r') as ts:
    fl = ts.readlines()
    print(type(fl[0]))







       
        final_data = []

        for i in range(0, len(data)):
            if i == 400:
                final_data.append(temp_data)
                temp_data = []
            temp_data[i%401] = data[i]

        json_data = json.dumps(final_data)

		with open(f'{self.imagePath}.json', 'w') as f:
            f.write(json_data)








	def generateJsCode(self):
    	#codeFile = open(f'{self.imagePath}.js', 'a')
    	#imageData = open(f'{self.imagePath}.csv', 'r')

		initCode = """ 

			function createPxl(height){
				var pixels = [];
				for(var i = 0; i < height; i++){
					for(var j = 0; j < 400; j++){
						var px = new Rectangle(1, 1);
						px.setPosition(j, i);
						var pixels_x = [];
						pixels_x[j] = px;
					}
					pixels[i] = pixels_x;
				}

				return pixels;
			}

			function setColor(pixels, pxPos, color){
				pixels[pxPos[0]][pxPos[1]].setColor(color);
			}

			function addPxs(pixels){
				for(var i = 0; i < pixels.length; i++){
					for(var j = 0; j < 400; j++){
						add(pixels[i][j]);
					}
				}
			}
		    			
		"""
		codeFile = open('code.js', 'a')
		codeFile.write(initCode)


		with open(f'{self.imagePath}.csv', 'r') as ts:
			data = ts.readlines()
			codeFile.write(f"createPxl({int(len(data)/400)});\n")
			codeFile.write(f""" 

				var data = {data};
				for(var i = 0; i < data.length; i++){{
					for(var j = 0; j < data[i].length; j++){{
						setColor(pixels, [i, j], data[i][j]);
					}}
				}}

			""")

		codeFile.close()

"""
		with open(f'{self.imagePath}.csv', 'r') as ts:
			data = ts.readlines()
			codeFile.write(f"createPxl({int(len(data)/400)});\n")
			for item in data:
				codeFile.write(f"setColor(pixels, [{data.index(item)%401}, {int(data.index(item)/400)}], {item});\n")

			codeFile.write("addPxs(pixels);")
"""