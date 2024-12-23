from typing import List, Optional

class Solution:
    def mesclarDuasListas(self, lista1: Optional[ListNode], lista2: Optional[ListNode]) -> Optional[ListNode]:
        if not lista1:
            return lista2
        if not lista2:
            return lista1

        if lista1.val < lista2.val:
            lista1.next = self.mesclarDuasListas(lista1.next, lista2)
            return lista1
        else:
            lista2.next = self.mesclarDuasListas(lista1, lista2.next)
            return lista2

    def mergeKLists(self, listas: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not listas:
            return None
        return self.dividirEConquistar(listas, 0, len(listas) - 1)

    def dividirEConquistar(self, listas: List[Optional[ListNode]], esquerda: int, direita: int) -> Optional[ListNode]:
        if esquerda == direita:
            return listas[esquerda]

        meio = esquerda + (direita - esquerda) // 2
        lista1 = self.dividirEConquistar(listas, esquerda, meio)
        lista2 = self.dividirEConquistar(listas, meio + 1, direita)
        return self.mesclarDuasListas(lista1, lista2)
