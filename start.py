import os
from ffmpy import FFmpeg

print('Please enter the path')
path=input('Path:')
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith('flac') or file.endswith('wav'):
            target_path=os.path.join(root, file)
            target_folder=os.path.dirname(target_path)
            target_base= os.path.basename(target_path)
            target_file_name=target_base.split('.')[0]
            print('Folder name:', target_folder)
            print('Base name:',target_base)
            print('Ready to convert..')
            convert_output_path=target_folder+'/'+target_file_name+'.mp3'
            ff = FFmpeg(inputs={target_path: None},
                        outputs={convert_output_path: '-q:a 0'})
            ff.run()
            print('OK:',convert_output_path)
