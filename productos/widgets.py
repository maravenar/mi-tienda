from django import forms
from django.utils.safestring import mark_safe

class ColorPickerWidget(forms.TextInput):
    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = '#000000'
        
        # Generar paleta completa con matices
        colors = []
        
        # Rojos
        colors.extend(['#FF0000', '#FF3333', '#FF6666', '#FF9999', '#FFCCCC'])
        colors.extend(['#CC0000', '#990000', '#660000', '#330000', '#FF4444'])
        
        # Naranjas
        colors.extend(['#FF8000', '#FF9933', '#FFB366', '#FFCC99', '#FFE6CC'])
        colors.extend(['#CC6600', '#994D00', '#663300', '#331A00', '#FF6600'])
        
        # Amarillos
        colors.extend(['#FFFF00', '#FFFF33', '#FFFF66', '#FFFF99', '#FFFFCC'])
        colors.extend(['#CCCC00', '#999900', '#666600', '#333300', '#FFCC00'])
        
        # Verdes
        colors.extend(['#00FF00', '#33FF33', '#66FF66', '#99FF99', '#CCFFCC'])
        colors.extend(['#00CC00', '#009900', '#006600', '#003300', '#00FF80'])
        
        # Azules
        colors.extend(['#0000FF', '#3333FF', '#6666FF', '#9999FF', '#CCCCFF'])
        colors.extend(['#0000CC', '#000099', '#000066', '#000033', '#0080FF'])
        
        # Púrpuras
        colors.extend(['#8000FF', '#9933FF', '#B366FF', '#CC99FF', '#E6CCFF'])
        colors.extend(['#6600CC', '#4D0099', '#330066', '#1A0033', '#FF00FF'])
        
        # Rosas
        colors.extend(['#FF0080', '#FF33A0', '#FF66C0', '#FF99E0', '#FFCCF0'])
        colors.extend(['#CC0066', '#99004D', '#660033', '#33001A', '#FF1493'])
        
        # Grises
        colors.extend(['#000000', '#333333', '#666666', '#999999', '#CCCCCC'])
        colors.extend(['#FFFFFF', '#F0F0F0', '#E0E0E0', '#D0D0D0', '#C0C0C0'])
        
        color_options = ''
        for i, color in enumerate(colors):
            if i % 10 == 0 and i > 0:
                color_options += '<br>'
            color_options += f'<div class="color-option" style="width: 20px; height: 20px; background-color: {color}; display: inline-block; margin: 1px; cursor: pointer; border: 1px solid #ddd; border-radius: 2px;" onclick="selectColor(\'{name}\', \'{color}\')" title="{color}"></div>'
        
        html = f'''
        <div class="color-picker-container">
            <input type="hidden" name="{name}" value="{value}" id="id_{name}">
            <div class="color-display" style="background-color: {value}; width: 60px; height: 40px; border: 2px solid #ddd; border-radius: 8px; cursor: pointer; display: inline-block; margin-right: 10px;" onclick="toggleColorPicker('{name}')"></div>
            <input type="text" value="{value}" style="width: 100px; font-family: monospace;" onchange="updateColor('{name}', this.value)">
            <div id="picker_{name}" class="color-palette" style="display: none; position: absolute; z-index: 1000; background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                <div class="color-grid">
                    {color_options}
                </div>
                <div style="margin-top: 10px;">
                    <input type="color" onchange="selectColor('{name}', this.value)" style="width: 100%; height: 40px; border: none; cursor: pointer;">
                </div>
            </div>
        </div>
        
        <script>
        function toggleColorPicker(name) {{
            const picker = document.getElementById('picker_' + name);
            picker.style.display = picker.style.display === 'none' ? 'block' : 'none';
        }}
        
        function selectColor(name, color) {{
            document.getElementById('id_' + name).value = color;
            const textInput = document.querySelector('#id_' + name).parentNode.querySelector('input[type="text"]');
            textInput.value = color;
            const colorDisplay = document.querySelector('#id_' + name).parentNode.querySelector('.color-display');
            colorDisplay.style.backgroundColor = color;
            document.getElementById('picker_' + name).style.display = 'none';
        }}
        
        function updateColor(name, color) {{
            if (/^#[0-9A-F]{{6}}$/i.test(color)) {{
                document.getElementById('id_' + name).value = color;
                const colorDisplay = document.querySelector('#id_' + name).parentNode.querySelector('.color-display');
                colorDisplay.style.backgroundColor = color;
            }}
        }}
        </script>
        '''
        
        return mark_safe(html)