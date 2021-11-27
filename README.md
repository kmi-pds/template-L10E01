# L10E01 - Spanning Tree Protocol

Naprogramujte zjednodušenou verzi Spanning Tree Protocol (všechny cesty v síti mají stejnou rychlost). Výsledný root uzel musí být uzel s nejmenším id (tedy 0). Vzorová topologie sítě pochází z tohoto článku: https://www.lewuathe.com/an-outline-of-spanning-tree-protocol.html.

Pro STP zprávy můžete použít vlastní `namedtuple` který obalíte do `Message` z knihovny `distsim`.