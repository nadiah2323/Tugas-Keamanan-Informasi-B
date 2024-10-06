
# Permutasi awal untuk data
PI = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# Permutasi awal yang di buat di key
CP_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

# Permutasi yang diterapkan pada shifted key untuk mendapat Ki+1
CP_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

# Expand matriks untuk mendapatkan matriks data 48 bit untuk menerapkan xor dengan Ki
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

#SBOX
S_BOX = [
         
[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
],

[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
],

[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
],

[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
],  

[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
], 

[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
], 

[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
],
   
[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]
]

#Permut made after each SBox substitution for each round
P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

#Final permut for datas after the 16 rounds
PI_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

# Matrix yang menentukan shift untuk setiap round key
SHIFT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

# Konversi string menjadi bit
def string_to_bit_array(text):
    array = list()
    for char in text:
        # Mendapat value char dalam 1 bit
        binval = binvalue(char, 8)
        # Menambahkan bit ke final list
        array.extend([int(x) for x in list(binval)])
    return array

# Menghasilkan string dari array bit
def bit_array_to_string(array): 
    res = ''.join([chr(int(y,2)) for y in [''.join([str(x) for x in _bytes]) for _bytes in  nsplit(array,8)]])   
    return res

# Mengembalikan nilai biner sebagai string dengan ukuran yang diberikan
def binvalue(val, bitsize): 
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise "binary value larger than the expected size"
    while len(binval) < bitsize:
        # Menambahkan 0 sebanyak yang diperlukan untuk mendapatkan ukuran yang diinginkan
        binval = "0"+binval 
    return binval

# Membagi daftar menjadi sub-daftar dengan ukuran "n"
def nsplit(s, n):
    return [s[k:k+n] for k in range(0, len(s), n)]

ENCRYPT=1
DECRYPT=0

class des():
    def __init__(self):
        self.password = None
        self.text = None
        self.keys = list()
        
    def run(self, key, text, action=ENCRYPT, padding=False):
        if len(key) < 8:
            raise Exception("Key harus 8 bytes")
        elif len(key) > 8:
            # Jika ukuran key lebih dari 8 byte, cut menjadi 8 byte
            key = key[:8] 

        self.password = key
        self.text = text
    
        if padding and action == ENCRYPT:
            self.addPadding()
        elif len(self.text) % 8 != 0:  # Jika tidak ada padding yang ditentukan, ukuran data harus kelipatan 8 byte
            raise Exception("Data size should be multiple of 8")
        
        # Menghasilkan semua key
        self.generatekeys()  
        # Membagi teks menjadi blok 8 byte (64 bit)
        text_blocks = nsplit(self.text, 8)
        result = list()
        # Loop melalui semua blok data
        for block in text_blocks:  
            # Mengubah blok menjadi array bit
            block = string_to_bit_array(block)  
            # Menerapkan permutasi awal
            block = self.permut(block, PI)
            # g (KIRI), d (KANAN)
            g, d = nsplit(block, 32)  
            tmp = None
            # Melakukan 16 putaran
            for i in range(16):  
                # Expand d untuk mencocokkan ukuran Ki (48 bit)
                d_e = self.expand(d, E)  
                if action == ENCRYPT:
                    # Jika enkripsi, gunakan Ki
                    tmp = self.xor(self.keys[i], d_e) 
                else:
                    # Jika dekripsi, mulai dengan key terakhir
                    tmp = self.xor(self.keys[15 - i], d_e) 
                # Metode yang akan menerapkan SBOX
                tmp = self.substitute(tmp)  
                tmp = self.permut(tmp, P)
                tmp = self.xor(g, tmp)
                g = d
                d = tmp
            # Melakukan permutasi terakhir dan menambahkan hasilnya
            result += self.permut(d + g, PI_1)
        final_res = bit_array_to_string(result)
        if padding and action == DECRYPT:
            # Menghapus padding jika dekripsi dan padding benar
            return self.removePadding(final_res)
        else:
            # Mengembalikan string akhir data yang telah dienkripsi/didekripsi
            return final_res 
        
    # Mengganti byte menggunakan SBOX
    def substitute(self, d_e):
        # Membagi array bit menjadi sub-daftar 6 bit
        subblocks = nsplit(d_e, 6)
        result = list()
        # Untuk semua sublist
        for i in range(len(subblocks)):
            block = subblocks[i]
            # Mendapatkan baris dengan bit pertama dan terakhir
            row = int(str(block[0])+str(block[5]),2)
            # Kolom adalah bit ke-2, ke-3, ke-4, ke-5
            column = int(''.join([str(x) for x in block[1:][:-1]]),2) 
            # Mengambil nilai di SBOX yang sesuai untuk round (i)
            val = S_BOX[i][row][column]
            # Mengubah nilai menjadi biner
            bin = binvalue(val, 4)
            # Dan menambahkannya ke daftar hasil
            result += [int(x) for x in bin]
        return result

    # Permutasi blok yang diberikan menggunakan tabel yang diberikan      
    def permut(self, block, table):  
        return [block[x-1] for x in table]

    # Melakukan hal yang sama seperti permutasi tetapi untuk lebih jelas dinamakan    
    def expand(self, block, table):  
        return [block[x-1] for x in table]
        
    # Menerapkan xor dan mengembalikan final list
    def xor(self, t1, t2):  
        return [x ^ y for x, y in zip(t1, t2)]
        
    # Algoritma yang menghasilkan semua kunci
    def generatekeys(self):  
        self.keys = []
        key = string_to_bit_array(self.password)
        # Menerapkan permutasi awal pada key
        key = self.permut(key, CP_1)  
        # Membagi menjadi (g->KIRI),(d->KANAN)
        g, d = nsplit(key, 28)  
        # Menerapkan 16 putaran
        for i in range(16):  
            # Menerapkan pergeseran yang terkait dengan putaran (tidak selalu 1)
            g, d = self.shift(g, d, SHIFT[i])  
            # Menggabungkan
            tmp = g + d  
            # Menerapkan permutasi untuk mendapatkan Ki
            self.keys.append(self.permut(tmp, CP_2))

    # Menggeser daftar dengan nilai yang diberikan
    def shift(self, g, d, n):  
        return g[n:] + g[:n], d[n:] + d[:n]
        
    # Menambahkan padding ke data menggunakan spesifikasi PKCS5.
    def addPadding(self):  
        pad_len = 8 - (len(self.text) % 8)
        self.text += pad_len * chr(pad_len)
        
    # Menghapus padding dari plaintext
    def removePadding(self, data):  
        pad_len = ord(data[-1])
        return data[:-pad_len]
        
    def encrypt(self, key, text, padding=False):
        return self.run(key, text, ENCRYPT, padding)
        
    def decrypt(self, key, text, padding=False):
        return self.run(key, text, DECRYPT, padding)
    
if __name__ == '__main__':
    # Input key
    key = input("Masukkan key (8 bytes): ")
    
    # Jika key panjangnya bukan 8 byte, ulangi input
    while len(key) != 8:
        print("Key tidak valid, ulangi memasukkan key")
        key = input("Masukkan key (8 bytes): ")
    
    # Input text
    text = input("Masukkan teks: ")  

    d = des()
    
    # Enkripsi
    encrypted_text = d.encrypt(key, text, padding=True)
    print("Enkripsi: %r" % encrypted_text)
    
    # Dekripsi
    decrypted_text = d.decrypt(key, encrypted_text, padding=True)
    print("Dekripsi: ", decrypted_text)

