import os
import json
import shutil

# test

# 폴더명 수정? [Circle(Artist)] Title (Parady) [Lang] [Uncensored?]

'''
함수화시 고려부분 시작
'''
baseDir = 'hitomi.dl/hitomi/' # BaseDir 지정
#filename = basedir + 'info.txt' # FileName 지정
'''
함수화시 고려부분 끝
'''

def HitomiDLConvHDoujinDL_JSON(baseDir, targetDir):
    
    filename =  baseDir + targetDir + '/info.txt'
    if False == os.path.isfile(filename):
        print('no file : '+ filename)
        return ''
    with open(filename, encoding="UTF-8") as f:
        raw_txt = f.read().splitlines() # Delete /n character
    mod_txt = []
    for i in range(0,len(raw_txt)): #Scan First Element to End
        if raw_txt[i] != '' : # Remove Blank Line
            mod_txt.append(raw_txt[i])
    print('Opened : ' + filename )
    '''
    gallery_num_str = ''
    Title_str = '' # Will Be Title
    Artist_str = '' # Will Be Artist
    Group_str = '' # Will be Circle
    Type_str = '' # Will be type
    Series_str = '' # Will be Series
    Character_str = '' # Will be Character
    Tags_list_raw = [] # Will Be Tags Bulk
    Language_str = '' # Will Be language
    '''

    text_gallery_num_str = '갤러리 넘버:' # raw text of  Gallery_num
    text_Title_str = '제목:' # raw text of  Title
    text_Artist_str = '작가:' # raw text of  Artist
    text_Group_str = '그룹:' # raw text of  Circle
    text_Type_str = '타입:' # raw text of  type
    text_Series_str = '시리즈:' # raw text of  Series
    text_Character_str = '캐릭터:' # raw text of  Character
    text_Tags_list_raw = '태그:' # raw text of  Tags Bulk
    text_Language_str = '언어:' # raw text of  language

    tag_text_list = [text_gallery_num_str,text_Title_str,text_Artist_str,text_Group_str,text_Type_str,text_Series_str,text_Character_str,text_Tags_list_raw,text_Language_str]
    #tag_list = [gallery_num_str,Title_str,Artist_str,Group_str,Type_str,Series_str,Character_str,Tags_list_raw,Language_str]
    extracted_tag_list = []# Extracted Tag List

    for i in range(0,len(mod_txt)): #Scan First Element to End
        # Batch Run of Taging
        for target_tag in tag_text_list:
            if mod_txt[i][0:len(target_tag)] == target_tag: # target tag Extract [str]
                extracted = mod_txt[i][len(target_tag)+1:]
                extracted_tag_list.append(mod_txt[i][len(target_tag)+1:])

    gallery_num_str = extracted_tag_list[0] # Will be Gallery_num
    Title_str       = extracted_tag_list[1] # Will Be Title
    Artist_list     = extracted_tag_list[2].split(', ') if type(extracted_tag_list[2].split(', ')) == list else list(extracted_tag_list[2]) # Will Be Artist - will be list?
    Group_list      = extracted_tag_list[3].split(', ') if type(extracted_tag_list[3].split(', ')) == list else list(extracted_tag_list[3]) # Will be Circle - will be list?
    Type_str        = extracted_tag_list[4] # Will be type
    Series_list      = extracted_tag_list[5].split(', ') if type(extracted_tag_list[5].split(', ')) == list else list(extracted_tag_list[5]) # Will be Parody
    Character_list  = extracted_tag_list[6].split(', ') if type(extracted_tag_list[6].split(', ')) == list else list(extracted_tag_list[6]) # Will be Character
    Tags_list_raw   = extracted_tag_list[7].split(', ') if type(extracted_tag_list[7].split(', ')) == list else list(extracted_tag_list[7]) # Will Be Tags Bulk
    Language_list   = extracted_tag_list[8].split(', ') if type(extracted_tag_list[8].split(', ')) == list else list(extracted_tag_list[8]) # Will Be language
    url_str         = 'https://hitomi.la/galleries/' + gallery_num_str + '.html' # Extract gallerynum and convert to hitomi.la address

    # 태그 분리 From  Tag List 
    # female
    # male
    # misc
    female_tag_list = []
    male_tag_list = []
    other_tag_list = []

    for i in range(0,len(Tags_list_raw)):
            if Tags_list_raw[i][0:len('female:')] =='female:': 
                female_tag_list.append(Tags_list_raw[i][len('female:'):])
            elif Tags_list_raw[i][0:len('male:')] =='male:':
                male_tag_list.append(Tags_list_raw[i][len('male:'):])
            else:
                other_tag_list.append(Tags_list_raw[i])





     ## JSON 파일 작업 시작

        # Replaced By Below Mod
        #file_path = "blank.json" # Import From File
        #with open(file_path + '', encoding='utf-8') as blankjsonfile:
        #    blankjson = json.load(blankjsonfile)
        #    print(blankjson)

    # import blank info.json structure
    info_blank_str = '''{
      "manga_info": {
        "title": "",
        "original_title": "",
        "author": [],
        "artist": [],
        "circle": [],
        "scanlator": [],
        "translator": [],
        "publisher": "",
        "description": "",
        "status": "",
        "chapters": null,
        "pages": "",
        "tags": {
          "female": [],
          "male": [],
          "misc": []
        },
        "type": "",
        "language": [],
        "released": "",
        "characters": [],
        "series": "",
        "parody": [],
        "url": ""
      }
    }'''


    info_blank_obj = json.loads(info_blank_str)
    blankjson = info_blank_obj
    title        = Title_str
    artist       = Artist_list
    circle       = Group_list
    #description  = Comment_str_strip
    #pages        = 
    #tags_all     = 
    tag_female   = female_tag_list
    tag_male     = male_tag_list
    tag_misc     = other_tag_list
    tag_type     = Type_str
    #tag_url      = 
    language     = Language_list
    #released     = Upload_time_str
    characters   = Character_list
    #series       = Series_str
    parody       = Series_list
    url          = url_str 

    #manga_info  =blankjson['manga_info'] # 망가정보 전체 
    blankjson['manga_info']['title'] = title      # 망가 정보 
    blankjson['manga_info']['artist'] = artist             # artist
    blankjson['manga_info']['circle'] = circle             # group -> circle
    blankjson['manga_info']['type'] = tag_type             # 

    #blankjson['manga_info']['description'] = description
    #pages       =blankjson['manga_info']['pages'] # 저자
    #tags_all    =blankjson['manga_info']['tags'] #태그전체
    blankjson['manga_info']['tags']['female'] = tag_female # female 태그
    blankjson['manga_info']['tags']['male'] = tag_male     # male  태그 
    blankjson['manga_info']['tags']['misc'] = tag_misc       # other -> misc
    blankjson['manga_info']['language'] = language # Lang Tag
    blankjson['manga_info']['type'] = tag_type # type 태그
    blankjson['manga_info']['characters'] = characters # characters 태그 
    #blankjson['manga_info']['series'] = series # Sereis 태그 

    #blankjson['manga_info']['released'] = released
    blankjson['manga_info']['parody'] = parody

    #tag_type    =blankjson['manga_info']['type'] # parody? 
    blankjson['manga_info']['url'] = url  # Gallery Number From Filedir to hitomi.la  url      
    print('Convert DIr : ' + ' OK! ')
    return blankjson

'''
## 함수끝 json 내보내줌 
exportFilename = 'export_hitomi.json'
with open(exportFilename, 'w', encoding='utf-8') as exportConverted: # Open json with utf-8 
        json.dump(blankjson, exportConverted, indent=4, ensure_ascii=False) #Prevent Char Crash With ensure_ascii=false

'''

#test = HitomiDLConvHDoujinDL_JSON(basedir,'(release) [Karube Guri] Warm Charge (decensored) (N／A) [Koreanuage]')

#dirExportTagList = test #['artist']

def dirModifier(dirExportTagJSON_obj) : #return correct directory of [Circle(Artist)] Title (Parady) [Lang] [Uncensored?] Based on connected json structure
    dirtagexport = dirExportTagJSON_obj # Assign object to modifier
    
    def lenTagTest(testList,testTag):
        if len(testList[testTag]) == 0 :
            return ''
        elif len(testList[testTag]) == 1 :
            return testList[testTag][0]
        else:
            return 'Multiple '+ testTag

    dirCircle = lenTagTest(dirtagexport['manga_info'],'circle').replace('/','-') #list
    dirArtist = lenTagTest(dirtagexport['manga_info'],'artist').replace('/','-') # list
    dirTitle = dirtagexport['manga_info']['title'] # str
    dirParady = lenTagTest(dirtagexport['manga_info'],'parody').replace('/','-') # list
    dirLang = lenTagTest(dirtagexport['manga_info'],'language').replace('/','-') # list
    dirGallryNum = dirtagexport['manga_info']['url'][28:-5]
    strDirUncensored =' [Uncensored]' # make uncensored dir
    isUncensored = ('uncensored' or 'Uncensored' or 'decensored' or 'Decensored') in dirtagexport['manga_info']['tags']['misc'] # if uncensored like tag is exsist, return true
    dirUncensored =  strDirUncensored  if isUncensored else '' # Check Uncensored
    modifiedDIR = '[' + dirCircle + '(' + dirArtist + ')] ' + dirTitle  + ' (' + dirParady + ') [' + dirLang + ']' + dirUncensored + ' - (' + dirGallryNum + ') By_HitomiDL'
    
    # 폴더명 드럽게 길어지는거 해결
    dirLenTest = 250 - len(modifiedDIR.encode("utf-8"))

    dirTitle_mod = ''
    if dirLenTest < 0:

        breaker  = ''
        breaker_index = int('-1')

        if '｜' in dirTitle:
            breaker = '｜'
            breaker_index = dirTitle.find('｜')
            dirTitle_mod = dirTitle[breaker_index+2:]

        else:
            dirTitle_mod = dirTitle.encode('utf-8')[:-(250 - len(modifiedDIR.encode("utf-8")) - (len(dirTitle)))].decode('utf-8', 'ignore')
        modifiedDIR_cap = '[' + dirCircle + '(' + dirArtist + ')] ' + dirTitle_mod  + ' (' + dirParady + ') [' + dirLang + ']' + dirUncensored + ' - (' + dirGallryNum + ') By_HitomiDL'

    else:
        modifiedDIR_cap = modifiedDIR

    print('Converted : ' + modifiedDIR_cap)
    return modifiedDIR_cap



moveDirTable_list = []
## 실제 경로에 대해 반복실행 시작! 
targetDir_List = os.listdir(baseDir) # ALl Folders name to list 
for targetDirectory_index in range(0,len(targetDir_List)): # Loop For ALl SubDir!!!!
    
    targetDirectory = targetDir_List[targetDirectory_index] # Indexnumber To Dir Name
    print('Converted ' + str(targetDirectory_index) + "/" +  str(len(targetDir_List)) + "num.") # Debugging
    converted_Obj_Json = HitomiDLConvHDoujinDL_JSON(baseDir, targetDirectory) # Covert Tag ANd Export json
    if converted_Obj_Json == '':
        print('Pass Faulty Dir : ' + targetDirectory )
    else :
        ### Moving Directory! 
        tempMovedir_list = []
        tempMovedir_list.append(targetDirectory)
        tempMovedir_list.append(dirModifier(converted_Obj_Json))
        moveDirTable_list.append(tempMovedir_list)

        ## Finally, Export json to info.json File
        exportFilename = baseDir + targetDirectory + '/info.json' #Set Export info.json Directory
        with open(exportFilename, 'w', encoding='utf-8') as exportConverted: # Open json with utf-8 
            json.dump(converted_Obj_Json, exportConverted, indent=4, ensure_ascii=False) #Prevent Char Crash With ensure_ascii=false

## 폴더 경로 일괄수정
baseDir_mod = baseDir[:-1]+'_mod/'
for indexnum in range(0,len(moveDirTable_list)):
    origDir = baseDir + moveDirTable_list[indexnum][0]
    moveDir = baseDir_mod + moveDirTable_list[indexnum][1]
    shutil.copytree(str(origDir),str(moveDir))

