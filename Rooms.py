current_room = 0
             # Room 0
room_list = [["Center Starting Room\nA Large empty room with a dim light hanging from the ceiling."
              "\nYou see a shiny object in the corner of the room."
              "\nUpon closer inspection you realize it’s a key and put it in your pocket."
              "\nYou notice doorways to your East, South, and West", None, 6, 1, 14, True],
             # Room 1
             ["Hallway 1\nNarrow hallway lined with bricks.\nThere are doors to the North and South.", 0, None, 2, None, False],
             # Room 2
             ["Cell Hall 1\nA large long room containing what seems to be prisoner cells lined along the East and West walls."
              "\nIt looks like the cells were trashed and there is garbage in all of them."
              "\nThere is a locked room to the East and the South.", 1, 21, 3, None, False],
             # Room 3
             ["Cell Hall 2\nLong room containing more prisoner cells for the first half of the room."
              "\nThe most south part of the room contains doors."
              "\nThe east door leads to the Men’s bathroom, the West door leads to the Women’s Washroom.", 2, 4, None, 5, False],
             # Room 4
             ["Men's Bathroom\nA medium sized room filled with white tiles and and a couple stalls and urinals."
              "\nThere is a door to the West. ", None, None, None, 3, False],
             # Room 5
             ["Women's Bathroom\nA medium sized room filled with white tiles and and a line of stalls along the South wall."
              "\nThere is a door to the East.", None, 3, None, None, False],
             # Room 6
             ["Long Corridor Part 1\nA skinny hallway lined with bricks."
              "\nThere are doors to the East, West and South.", None, 7, 22, 0, False],
             # Room 7
             ["Long Corridor Part 2\nA skinny hallway lined with bricks."
              "\nThere are doors to the East, West and North.", 12, 8, None, 6, False],
             # Room 8
             ["Long Corridor Part 3\nA skinny hallway lined with bricks."
              "\nThere are doors to the East and West.", None, 9, None, 7, False],
             # Room 9
             ["Storage Room\nA large square room filled with old broken tools and supplies."
              "\nIt looks like no one has been here for at least 20 years."
              "\nThere are doors to the North, West, and South.", 10, None, 11, 8, False],
             # Room 10
             ["Electrical Room\nA large square room filled with large electrical panels and what looks to be a generator."
              "\nThe walls are lined with breakers and many switches."
              "\nThere is a door to the South", None, None, 9, None, False],
             # Room 11
             ["Weaponry\nA large square room with many cabinets lining the floor and walls of the room."
              "\nOne cabinet is open and it is filled with many weapons and corresponding ammunition."
              "\nThere are doors to the North and West", 9, None, None, 21, False],
             # Room 12
             ["Medical Room\nA rectangular room filled with gurneys and tables."
              "\nThere are cabinets in the room filled with medical equipment and medication that seems to have been emptied."
              "\nThere is a door to the South and a locked door to the West", None, None, 7, 13, False],
             # Room 13
             ["Employee Room\nA larger rectangular room with couches and TVs."
              "\nThere is a broken table in the center of the room."
              "\nThere is a door to the East.", None, 12, None, None, False],
             # Room 14
             ["Library\nA large room lined from floor to ceiling with shelves of books with many tables and chairs in the room."
              "\nThere are doors to the North and East.", 17, 0, 15, None, False],
             # Room 15
             ["Secret Library Corridor\nSecret hall hidden behind one of the shelves in the library."
              "\nThere is another door to the South", 14, None, 16, None, False],
             # Room 16
             ["Secret Lab\nA large room filled with lots of testing equipment and scientific apparati."
              "\nThere are cages in the Southwest corner that have bite marks on it."
              "\nThere is a door to the North", 15, None, None, None, False],
             # Room 17
             ["Outside Courtyard\nA large outdoor area surrounded by 20 foot high brick walls."
              "\nThere is workout equipment in the Northwest corner and a basketball net on the East wall."
              "\nThere is a door to the North and South.", 18, None, 14, None, False],
             # Room 18
             ["Security/ Surveillance Office\nA medium sized square room filled with tables with screens and the accompanying control boards on them."
              "\nThere is a door to the South and East.", None, 19, 17, None, False],
             # Room 19
             ["Head Office\nA Rectangular room with a large wooden desk in the center of it."
              "\nThis room seems to have been preserved the best out of all of them as it seems to be untouched."
              "\nThere are doors to the East and West.", None, 20, None, 18, False],
             # Room 20
             ["Escape\nSmall hallway containing a door to the East and West."
              "\nThe West door leads to the outside.", None, 20, None, 19, False],
             # Room 21
             ["Cell-Weaponry Corridor\nA long corridor running East-West that connects Cell Hall 1 and the Weaponry."
              "\nThere are doors to the East and West.", None, 11, None, 2, False],
             # Room 22
             ["Kitchen\nA Medium sized room filled with many kitchen appliances and stoves."
              "\nThere is a large metal table in the middle of the room that looks like it was used to prepare food on at one point."
              "\nThere is a door to the North", 6, None, None, None, False]]