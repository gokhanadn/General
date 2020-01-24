import cv2
import numpy as np

def main():
    dragon = cv2.imread("/home/gokhan/Pictures/Wallpapers/1094574.jpg")
    spacex = cv2.imread("/home/gokhan/Pictures/Wallpapers/wp2284541.jpg")

    spacex_grey = cv2.cvtColor(spacex,cv2.COLOR_BGR2GRAY) # Siyah-beyaz yaptım.

    #Bu bölüm internetten alındı. Resmi aynı ölçekte küçültmek için önemli!!!
    scale_percent = 40 # percent of original size
    width = int(dragon.shape[1] * scale_percent / 100)
    height = int(dragon.shape[0] * scale_percent / 100)
    dim = (width, height)

    new_dragon = cv2.resize(dragon, dim, interpolation = cv2.INTER_AREA)
    new_spacex = cv2.resize(spacex_grey, dim, interpolation = cv2.INTER_AREA)
    new_spacex_text = new_spacex[320:500,270:1450]

    #'Spacex' yazısının dragon resminin tam ortasına gelmesi için her iki resmi de 'Spacex' yazısına göre kestim.
    cv2.imshow("dragon",new_dragon[342:522,178:1358])  
    cv2.imshow("spacex",new_spacex[320:500,270:1450])

    ret, mask = cv2.threshold(new_spacex_text,128,255,cv2.THRESH_BINARY) # 128 üzerinde olan pixelleri beyaz, altındakileri siyah yapıyor.

    mask_inver = cv2.bitwise_not(mask) # Siyah olan pixeller ile beyaz olan pixellerin yerini değiştiriyor.
    cv2.imshow("MASK",mask)
    cv2.imshow("Ters-Mask",mask_inver)



    dragon_text = cv2.bitwise_and(new_dragon[342:522,178:1358],new_dragon[342:522,178:1358], mask = mask_inver) #İlk paramtere hangi resmi kullandığımız, ikincisi hangi resme göderdiğimizi, 'mask' parametresinde iste mask işlemini giriyoruz.
    cv2.imshow("Dragon_text",dragon_text)

#####################

    #dragon_text_grey = cv2.cvtColor(dragon_text,cv2.COLOR_BGR2GRAY)
    #cv2.imshow("dragon_text_grey",dragon_text_grey)

    toplam = cv2.add(dragon_text,  ) #İki resmi birleştiriyorum.
    cv2.imshow("Toplam",toplam)

    new_dragon[342:522,178:1358] = toplam #Son işlem: Yaptığım düzeltmeyi ana resme ekliyorum.
    cv2.imshow("Son hal",new_dragon)


    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()