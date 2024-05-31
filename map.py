#Defining the map as a list of list, representing different areas 
map = [
  [0, 1, 2,],
  [3, 4, 5,],
  [6, 7, 8]
]



# I added both the areas and the interactable things withint my game in dictionary
areas = {
  0: {"description": "Limgrave: Rolling hills and the occasional crumbling ruin. A gentle introduction to a harsh world" , 
     "Interactables":{"Sword" : "A rusty old sword stuck in the ground"}},
  1: {"description": "Stormveil Castle : A massive fortress guarded by formidable foes. The sound of clanking armor fills the air", 
     "Interactables" : {"Shield" : "A sturdy shield abandoned by a fallen knight"}},
  2: {"description" : "Mistwood: Dense fog and eerie silence , home to unseen creatures lurking in the shadowns. ",
     "Interactables" : {"amulet" : "An ancient amulet, glowing softly in the fog."}},
  3: {"description": "Caelid: A desolate Landscape, tainted by a scarlet rot that consumes all life."
     "Interactables" : {"Herbs": "A rare medical herb resistant to the rot."}},
  4: {"description" : "Raya lucardia academy: A centre of learning and magic, surrounded by water and mystery.", 
     "Interactables" : {"book": "A tome of forgotten spells left on a dusty shelf"}},
  5: {"description" : "Siofra River: An underground cavern with a river that glows with an eternal light.",
     "Interactables" : {"crystal" : "A luminous crystal by the river's edge."}},
  6: {"description" :"Mountains of Giants: Snow covered peaks and the reminicants of ancient Giants.",
     "Interactables" : {"Horns" : "A Giants horn, carved into a wild instrument"}},
  7: {"description" : "Eternal City: Ruins filled with the secrets of lost civilizations and guarded by spectral figures.",
     "Interactables" : {"Mask" : "A mysterious mask , floating above an altar,"}},
  8: {"description" : "Faraum Azula: Floating islands above a sea of clouds the domain of dragons and lightning.",
     "Interactables" : {"scale" :"A dragon scale, shimmering with energy."}}
}