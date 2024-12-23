class Solution:
    def findMedianSortedArrays(self, lista1, lista2):
        n1 = len(lista1)
        n2 = len(lista2)

        if n1 > n2:
            return self.findMedianSortedArrays(lista2, lista1)

        n = n1 + n2
        esquerda = (n1 + n2 + 1) // 2
        baixo = 0
        alto = n1

        while baixo <= alto:
            meio1 = (baixo + alto) // 2
            meio2 = esquerda - meio1

            esquerdo1 = float('-inf')
            esquerdo2 = float('-inf')
            direito1 = float('inf')
            direito2 = float('inf')

            if meio1 < n1:
                direito1 = lista1[meio1]
            if meio2 < n2:
                direito2 = lista2[meio2]
            if meio1 - 1 >= 0:
                esquerdo1 = lista1[meio1 - 1]
            if meio2 - 1 >= 0:
                esquerdo2 = lista2[meio2 - 1]

            if esquerdo1 <= direito2 and esquerdo2 <= direito1:
                if n % 2 == 1:
                    return max(esquerdo1, esquerdo2)
                else:
                    return (max(esquerdo1, esquerdo2) + min(direito1, direito2)) / 2.0
            elif esquerdo1 > direito2:
                alto = meio1 - 1
            else:
                baixo = meio1 + 1

        return 0
