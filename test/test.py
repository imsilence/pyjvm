#encoding: utf-8

from struct import unpack

'''
1 B
2 H
4 L
8 Q

4 f
8 d

'''

if __name__ == '__main__':
    cxt = open('HelloWorld.class', 'rb').read()

    print(unpack('>L', cxt[:4])) #magic

    print(unpack('>HH', cxt[4:8])) # version minor major

    print(unpack('>H', cxt[8:10])) # constant pool [1, 48)

    pool = []
    print(unpack('>B', cxt[10:11])) # 1.type
    print(unpack('>HH', cxt[11:15])) # methodref classIndex, nameAndTypeIndex

    print(unpack('>B', cxt[15:16])) # 2.type
    print(unpack('>HH', cxt[16:20])) # fieldref classIndex, nameAndTypeIndex

    print(unpack('>B', cxt[20:21])) # 3.type
    print(unpack('>H', cxt[21:23])) # string index

    print(unpack('>B', cxt[23:24])) # 4.type
    print(unpack('>HH', cxt[24:28])) # fieldref classIndex, nameAndTypeIndex

    print(unpack('>B', cxt[28:29])) # 5.type
    print(unpack('>HH', cxt[29:33])) # fieldref classIndex, nameAndTypeIndex

    print(unpack('>B', cxt[33:34])) # 6.type
    print(unpack('>f', cxt[34:38])) # float

    print(unpack('>B', cxt[38:39])) # 7.type
    print(unpack('>HH', cxt[39:43])) # fieldref classIndex, nameAndTypeIndex

    print(unpack('>B', cxt[43:44])) # 8.type
    print(unpack('>HH', cxt[44:48])) # fieldref classIndex, nameAndTypeIndex

    print(unpack('>B', cxt[48:49])) # 9.type
    print(unpack('>H', cxt[49:51])) # string index

    print(unpack('>B', cxt[51:52])) # 10.type
    print(unpack('>HH', cxt[52:56])) # methodref classIndex, nameAndTypeIndex

    print(unpack('>B', cxt[56:57])) # 11.type
    print(unpack('>H', cxt[57:59])) # class index

    print(unpack('>B', cxt[59:60])) # 12.type
    print(unpack('>H', cxt[60:62])) # class index

    print(unpack('>B', cxt[62:63])) # 13.type
    print(unpack('>H', cxt[63:65])) # utf8 length
    print(unpack('>3s', cxt[65:68])) # utf8

    print(unpack('>B', cxt[68:69])) # 14.type
    print(unpack('>H', cxt[69:71])) # utf8 length
    print(unpack('>s', cxt[71:72])) # utf8

    print(unpack('>B', cxt[72:73])) # 15.type
    print(unpack('>H', cxt[73:75])) # utf8 length
    print(unpack('>4s', cxt[75:79])) # utf8

    print(unpack('>B', cxt[79:80])) # 16.type
    print(unpack('>H', cxt[80:82])) # utf8 length
    print(unpack('>18s', cxt[82:100])) # utf8

    print(unpack('>B', cxt[100:101])) # 17.type
    print(unpack('>H', cxt[101:103])) # utf8 length
    print(unpack('>3s', cxt[103:106])) # utf8

    print(unpack('>B', cxt[106:107])) # 18.type
    print(unpack('>H', cxt[107:109])) # utf8 length
    print(unpack('>s', cxt[109:110])) # utf8

    print(unpack('>B', cxt[110:111])) # 19.type
    print(unpack('>H', cxt[111:113])) # utf8 length
    print(unpack('>6s', cxt[113:119])) # utf8

    print(unpack('>B', cxt[119:120])) # 20.type
    print(unpack('>H', cxt[120:122])) # utf8 length
    print(unpack('>s', cxt[122:123])) # utf8

    print(unpack('>B', cxt[123:124])) # 21.type
    print(unpack('>H', cxt[124:126])) # utf8 length
    print(unpack('>6s', cxt[126:132])) # utf8

    print(unpack('>B', cxt[132:133])) # 22.type
    print(unpack('>H', cxt[133:135])) # utf8 length
    print(unpack('>3s', cxt[135:138])) # utf8

    print(unpack('>B', cxt[138:139])) # 23.type
    print(unpack('>H', cxt[139:141])) # utf8 length
    print(unpack('>4s', cxt[141:145])) # utf8

    print(unpack('>B', cxt[145:146])) # 24.type
    print(unpack('>H', cxt[146:148])) # utf8 length
    print(unpack('>15s', cxt[148:163])) # utf8

    print(unpack('>B', cxt[163:164])) # 25.type
    print(unpack('>H', cxt[164:166])) # utf8 length
    print(unpack('>4s', cxt[166:170])) # utf8

    print(unpack('>B', cxt[170:171])) # 26.type
    print(unpack('>H', cxt[171:173])) # utf8 length
    print(unpack('>22s', cxt[173:195])) # utf8

    print(unpack('>B', cxt[195:196])) # 27.type
    print(unpack('>H', cxt[196:198])) # utf8 length
    print(unpack('>10s', cxt[198:208])) # utf8

    print(unpack('>B', cxt[208:209])) # 28.type
    print(unpack('>H', cxt[209:211])) # utf8 length
    print(unpack('>15s', cxt[211:226])) # utf8

    print(unpack('>B', cxt[226:227])) # 29.type
    print(unpack('>HH', cxt[227:231])) # nameAndType name descriptor index

    print(unpack('>B', cxt[231:232])) # 30.type
    print(unpack('>HH', cxt[232:236])) # nameAndType name descriptor index

    print(unpack('>B', cxt[236:237])) # 31.type
    print(unpack('>H', cxt[237:239])) # utf8 length
    print(unpack('>2s', cxt[239:241])) # utf8

    print(unpack('>B', cxt[241:242])) # 32.type
    print(unpack('>HH', cxt[242:246])) # nameAndType name descriptor index

    print(unpack('>B', cxt[246:247])) # 33.type
    print(unpack('>HH', cxt[247:251])) # nameAndType name descriptor index

    print(unpack('>B', cxt[251:252])) # 34.type
    print(unpack('>HH', cxt[252:256])) # nameAndType name descriptor index

    print(unpack('>B', cxt[256:257])) # 35.type
    print(unpack('>H', cxt[257:259])) # class name index

    print(unpack('>B', cxt[259:260])) # 36.type
    print(unpack('>HH', cxt[260:264])) # nameAndType name descriptor index

    print(unpack('>B', cxt[264:265])) # 37.type
    print(unpack('>H', cxt[265:267])) # utf8 length
    print(unpack('>14s', cxt[267:281])) # utf8

    print(unpack('>B', cxt[281:282])) # 38.type
    print(unpack('>H', cxt[282:284])) # class name index

    print(unpack('>B', cxt[284:285])) # 39.type
    print(unpack('>HH', cxt[285:289])) # nameAndType name descriptor index

    print(unpack('>B', cxt[289:290])) # 40.type
    print(unpack('>H', cxt[290:292])) # utf8 length
    print(unpack('>10s', cxt[292:302])) # utf8

    print(unpack('>B', cxt[302:303])) # 41.type
    print(unpack('>H', cxt[303:305])) # utf8 length
    print(unpack('>16s', cxt[305:321])) # utf8

    print(unpack('>B', cxt[321:322])) # 42.type
    print(unpack('>H', cxt[322:324])) # utf8 length
    print(unpack('>16s', cxt[324:340])) # utf8

    print(unpack('>B', cxt[340:341])) # 43.type
    print(unpack('>H', cxt[341:343])) # utf8 length
    print(unpack('>3s', cxt[343:346])) # utf8

    print(unpack('>B', cxt[346:347])) # 44.type
    print(unpack('>H', cxt[347:349])) # utf8 length
    print(unpack('>21s', cxt[349:370])) # utf8

    print(unpack('>B', cxt[370:371])) # 45.type
    print(unpack('>H', cxt[371:373])) # utf8 length
    print(unpack('>19s', cxt[373:392])) # utf8

    print(unpack('>B', cxt[392:393])) # 46.type
    print(unpack('>H', cxt[393:395])) # utf8 length
    print(unpack('>7s', cxt[395:402])) # utf8

    print(unpack('>B', cxt[402:403])) # 47.type
    print(unpack('>H', cxt[403:405])) # utf8 length
    print(unpack('>21s', cxt[405:426])) # utf8

    print(unpack('>H', cxt[426:428])) #access flags

    print(unpack('>H', cxt[428:430])) #this class

    print(unpack('>H', cxt[430:432])) #super class

    print(unpack('>H', cxt[432:434])) # interfaces count

    #print(unpack('>H', cxt[434:436])) #interfaces

    print(unpack('>H', cxt[434:436])) # fields count

    print(unpack('>H', cxt[436:438])) # fields.1.access_flags
    print(unpack('>H', cxt[438:440])) # fields.1.nameIndex
    print(unpack('>H', cxt[440:442])) # fields.1.descriptorIndex
    print(unpack('>H', cxt[442:444])) # fields.1.attrs.count

    print(unpack('>H', cxt[444:446])) # fields.2.access_flags
    print(unpack('>H', cxt[446:448])) # fields.2.nameIndex
    print(unpack('>H', cxt[448:450])) # fields.2.descriptorIndex
    print(unpack('>H', cxt[450:452])) # fields.2.attrs.count

    print(unpack('>H', cxt[452:454])) # fields.3.access_flags
    print(unpack('>H', cxt[454:456])) # fields.3.nameIndex
    print(unpack('>H', cxt[456:458])) # fields.3.descriptorIndex
    print(unpack('>H', cxt[458:460])) # fields.3.attrs.count


    print(unpack('>H', cxt[460:462])) # fields.4.access_flags
    print(unpack('>H', cxt[462:464])) # fields.4.nameIndex
    print(unpack('>H', cxt[464:466])) # fields.4.descriptorIndex
    print(unpack('>H', cxt[466:468])) # fields.4.attrs.count

    print(unpack('>H', cxt[468:470])) # methods count

    print(unpack('>H', cxt[470:472])) # methods.1.access_flags
    print(unpack('>H', cxt[472:474])) # methods.1.nameIndex
    print(unpack('>H', cxt[474:476])) # methods.1.descriptorIndex
    print(unpack('>H', cxt[476:478])) # methods.1.attrs.count
