#! /usr/bin/python
import xml.etree.ElementTree as ET
import sys

mii = {}

def readBinaryMii(filename):
    miidata = []
    with open(filename, "rb") as f:
        while (byte := f.read(1)):
            miidata.append(int.from_bytes(byte, byteorder='big'))
            #print(int.from_bytes(byte, byteorder='big'))
    f.close()
    
    # Bytes 0x18 and 0x19
    mii['sex'] = miidata[0x18] & 1
    mii['bmonth'] = (miidata[0x18]>>1) & 15
    bday1 = (miidata[0x18]>>5) & 7
    bday2 = (miidata[0x19]) & 3
    mii['bday'] = bday1 | (bday2<<3)
    mii['color'] = (miidata[0x19]>>2) & 15
    mii['favorite'] = (miidata[0x19]>>6) & 1

    # Byte 0x30
    mii['sharing'] = (miidata[0x30]) & 1
    mii['face'] = (miidata[0x30]>>1) & 15
    mii['skin'] = (miidata[0x30]>>5) & 7

    # Byte 0x31
    mii['wrinkles'] = (miidata[0x31]) & 15
    mii['makeup'] = (miidata[0x31]>>4) & 15

    # Byte 0x32
    mii['hair'] = miidata[0x32]

    # Byte 0x33
    mii['haircol'] = miidata[0x33] & 7
    mii['hairflip'] = (miidata[0x31]>>3) & 1

    # Bytes 0x34-0x37
    mii['eye'] = miidata[0x34] & 63
    eyecol1 = (miidata[0x34]>>6) & 3
    eyecol2 = (miidata[0x35]) & 1
    mii['eyecol'] = eyecol1 | (eyecol2<<2)
    mii['eyescale'] = (miidata[0x35]>>1) & 15
    mii['eyeaspect'] = (miidata[0x35]>>5) & 7
    mii['eyerot'] = miidata[0x36] & 31
    eyex1 = (miidata[0x36]>>5) & 7
    eyex2 = (miidata[0x37]) & 1
    mii['eyex'] = eyex1 | (eyex2<<3)
    mii['eyey'] = (miidata[0x37]>>1) & 31

    # Bytes 0x38-0x3B
    mii['brow'] = miidata[0x38] & 31
    mii['browcol'] = (miidata[0x38]>>5) & 7
    mii['browscale'] = miidata[0x39] & 15
    mii['browaspect'] = (miidata[0x39]>>4) & 7
    mii['browrot'] = miidata[0x3A] & 15
    browx1 = (miidata[0x3A]>>5) & 7
    browx2 = (miidata[0x3B]) & 1
    mii['browx'] = browx1 | (browx2<<3)
    mii['browy'] = (miidata[0x3B]>>1) & 31

    # Bytes 0x3C-0x3D
    mii['nose'] = miidata[0x3C] & 31
    nosesc1 = (miidata[0x3C]>>5) & 7
    nosesc2 = (miidata[0x3D]) & 1
    mii['nosescale'] = nosesc1 | (nosesc2<<3)
    mii['nosey'] = (miidata[0x3D]>>1) & 31

    # Bytes 0x3E-0x40
    mii['mouth'] = miidata[0x3E] & 63
    mouthcol1 = (miidata[0x3E]>>6) & 3
    mouthcol2 = (miidata[0x3F]) & 1
    mii['mouthcol'] = mouthcol1 | (mouthcol2<<2)
    mii['mouthscale'] = (miidata[0x3F]>>1) & 15
    mii['mouthaspect'] = (miidata[0x3F]>>5) & 7
    mii['mouthy'] = miidata[0x40] & 31
    mii['mustache'] = (miidata[0x40]>>5) & 7

    # Bytes 0x42-0x43
    mii['beard'] = miidata[0x42] & 7
    mii['beardcol'] = (miidata[0x42]>>3) & 7
    mustsc1 = (miidata[0x42]>>6) & 3
    mustsc2 = (miidata[0x43]) & 3
    mii['mustscale'] = mustsc1 | (mustsc2<<2)
    mii['musty'] = (miidata[0x43]>>2) & 31

    # Bytes 0x44-0x45
    mii['glasses'] = miidata[0x44] & 15
    mii['glassescol'] = (miidata[0x44]>>4) & 7
    glscl1 = (miidata[0x44]>>7) & 1
    glscl2 = miidata[0x45] & 7
    mii['glassesscale'] = glscl1 | (glscl2<<1)
    mii['glassesy'] = (miidata[0x45]>>3) & 31

    # Bytes 0x46-0x47
    mii['mole'] = miidata[0x46] & 1
    mii['molescale'] = (miidata[0x46]>>1) & 15
    molex1 = (miidata[0x46]>>5) & 7
    molex2 = miidata[0x47] & 3
    mii['molex'] = molex1 | (molex2<<3)
    mii['moley'] = (miidata[0x47]>>2) & 31

    print("Birth Month:\t"+str(mii['bmonth']))
    print("Birth Day:\t"+str(mii['bday']))
    print("Fav Color:\t"+str(mii['color']))
    print("Face Shape:\t"+str(mii['face']))
    print("Skin Col:\t"+str(mii['skin']))
    print()

    print("Wrinkles:\t"+str(mii['wrinkles']))
    print("Makeup:\t\t"+str(mii['makeup']))
    print()

    print("Hairstyle:\t"+str(mii['hair']))
    print("Hair Col:\t"+str(mii['haircol']))
    print("Hair Flip:\t"+str(mii['hairflip']))
    print()

    print("Eye Style:\t"+str(mii['eye']))
    print("Eye Col:\t"+str(mii['eyecol']))
    print("Eye Scale:\t"+str(mii['eyescale']))
    print("Eye YScale:\t"+str(mii['eyeaspect']))
    print("Eye Rotate:\t"+str(mii['eyerot']))
    print("Eye X Sp:\t"+str(mii['eyex']))
    print("Eye Y:\t\t"+str(mii['eyey']))
    print()

    print("Brow Style:\t"+str(mii['brow']))
    print("Brow Col:\t"+str(mii['browcol']))
    print("Brow Scale:\t"+str(mii['browscale']))
    print("Brow YScale:\t"+str(mii['browaspect']))
    print("Brow Rotate:\t"+str(mii['browrot']))
    print("Brow X Sp:\t"+str(mii['browx']))
    print("Brow Y:\t\t"+str(mii['browy']))
    print()

    print("Nose Type:\t"+str(mii['nose']))
    print("Nose Scale:\t"+str(mii['nosescale']))
    print("Nose Y:\t\t"+str(mii['nosey']))
    print()

    print("Mouth Type:\t"+str(mii['mouth']))
    print("Mouth Col:\t"+str(mii['mouthcol']))
    print("Mouth Scale:\t"+str(mii['mouthscale']))
    print("Mouth YScale:\t"+str(mii['mouthaspect']))
    print("Mustache:\t"+str(mii['mustache']))
    print()

    print("Beard Type:\t"+str(mii['beard']))
    print("Beard Col:\t"+str(mii['beardcol']))
    print("Must Scale:\t"+str(mii['mustscale']))
    print("Must Y:\t\t"+str(mii['musty']))
    print()

    print("Glasses:\t"+str(mii['glasses']))
    print("Glass Col:\t"+str(mii['glassescol']))
    print("Glass Scale:\t"+str(mii['glassesscale']))
    print("Glass Y:\t"+str(mii['glassesy']))

def writeUMii(filename, outfilename):
    tree = ET.parse(filename)
    root = tree.getroot()

    tshape = root.find('shape')
    thair = root.find('hair')
    teye = root.find('eye')
    teyebrow = root.find('eyebrow')
    tnose = root.find('nose')
    tmouth = root.find('mouth')
    tbeard = root.find('beard')
    tglass = root.find('glass')

    # Mii Parameters
    face = tshape.find('jaw')
    face.text = str(mii['face'])
    skin = tshape.find('skin_color')
    skin.text = str(mii['skin'])
    wrinkles = tshape.find('wrinkle')
    wrinkles.text = str(mii['wrinkles'])
    makeup = tshape.find('make')
    makeup.text = str(mii['skin'])
    
    hair = thair.find('type')
    hair.text = str(mii['hair'])
    haircol = thair.find('color')
    haircol.text = str(mii['haircol'])
    hairflip = thair.find('flip')
    hairflip.text = str(mii['hairflip'])
    
    eye = teye.find('type')
    eye.text = str(mii['eye'])
    eyecol = teye.find('color')
    eyecol.text = str(mii['eyecol'])
    eyescale = teye.find('scale')
    eyescale.text = str(mii['eyescale'])
    eyeaspect = teye.find('aspect')
    eyeaspect.text = str(mii['eyeaspect'])
    eyerot = teye.find('rotate')
    eyerot.text = str(0-float(mii['eyerot'])/10)
    eyex = teye.find('trans_u')
    eyex.text = str(mii['eyex'])             
    eyey = teye.find('trans_v')
    eyey.text = str(mii['eyey'])

    brow = teyebrow.find('type')
    brow.text = str(mii['brow'])
    browcol = teyebrow.find('color')
    browcol.text = str(mii['browcol'])
    browscale = teyebrow.find('scale')
    browscale.text = str(mii['browscale'])
    browaspect = teyebrow.find('aspect')
    browaspect.text = str(mii['browaspect'])
    browrot = teyebrow.find('rotate')
    browrot.text = str(0-float(mii['browrot']/10))
    browx = teyebrow.find('trans_u')
    browx.text = str(mii['browx'])
    browy = teyebrow.find('trans_v')
    browy.text = str(mii['browy']-3)

    nose = tnose.find('type')
    nose.text = str(mii['nose'])
    nosescale = tnose.find('scale')
    nosescale.text = str(mii['nosescale'])
    nosey = tnose.find('trans_v')
    nosey.text = str(mii['nosey'])

    mouth = tmouth.find('type')
    mouth.text = str(mii['mouth'])
    mouthcol = tmouth.find('color')
    mouthcol.text = str(mii['mouthcol'])
    mouthscale = tmouth.find('scale')
    mouthscale.text = str(mii['mouthscale'])
    mouthaspect = tmouth.find('aspect')
    mouthaspect.text = str(mii['mouthaspect'])
    
    mustache = tbeard.find('mustache')
    mustache.text = str(mii['mustache'])
    beard = tbeard.find('type')
    beard.text = str(mii['beard'])
    beardcol = tbeard.find('color')
    beardcol.text = str(mii['beardcol'])
    mustscale = tbeard.find('scale')
    mustscale.text = str(mii['mustscale'])

    glasses = tglass.find('type')
    glasses.text = str(mii['glasses'])
    glassescol = tglass.find('color')
    glassescol.text = str(mii['glassescol'])

    tree.write(outfilename)

def main():
    if len(sys.argv) < 3:
        print("Usage: yewmiiconv miifile.mii input.bumii.xml output.bumii.xml")
        return(1)

    miifilename = sys.argv[1]
    xmlfilename = sys.argv[2]
    outfilename = sys.argv[3]

    readBinaryMii(miifilename)
    writeUMii(xmlfilename, outfilename)

if __name__ == "__main__":
    main()

