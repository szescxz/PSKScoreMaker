# coding=utf-8
import sys
import re
import scoremaker

#####  define  #####
music_info_key_word = {
    'bpm': '#BPM01: (\d*)',
}
#####  read file  ######
def read_file(file_name):
    file_object = open('musicscore/' + file_name,'r')

    music_info = {}
    music_score = []

    read_step = 0
    try:
        for line in file_object:
            if read_step == 0:
                # get music info
                for key_word in music_info_key_word:
                    info = re.match(music_info_key_word[key_word], line)
                    if info:
                        music_info[key_word] = info.group(1)

            # get music score
            if line == '#MEASUREHS 00\n':
                read_step += 1
                continue

            if read_step == 1:
                info = re.match('#(\d\d\d)(\d)([0-9a-f]):(\w*)', line)

                if info:
                    music_score.append({
                        'unitid': info.group(1),
                        'type': info.group(2),
                        'row': info.group(3),
                        'list': info.group(4),
                    })
                    continue

                info = re.match('#(\d\d\d)(\d)([0-9a-f])(\d):(\w*)', line)
                if info:
                    music_score.append({
                        'unitid': info.group(1),
                        'type': info.group(2),
                        'row': info.group(3),
                        'longid': info.group(4),
                        'list': info.group(5),
                    })
                    continue

    finally:
        for key_word in music_info_key_word:
            if key_word not in music_info:
                music_info[key_word] = 'No info'

        file_object.close()

    music_score.sort(key=lambda x: x['unitid'])

    return music_info, music_score

def run(file_name):
    music_info, music_score = read_file(file_name)
    score_image = scoremaker.create_image(music_info, music_score)
    print('music information:\nBPM:%s' % (music_info['bpm']))
    score_image.show()

def main(argv):
    run(argv[0])

if __name__ == "__main__":
    main(sys.argv[1:])