Rooms = {
  'road': {
    'key': 'road',
    'name': 'Dusty Dirt Road',
    'description': 
    '''You are standing on the dusty road that leads from your village to Blackwood in the east. On the north side a path leads into the forest.''',
    'exits': {
      'north': 'forest'
    }
  },
  'forest': {
    'key': 'forest',
    'name': 'Dim Forest',
    'description':
    '''The forest is thick with growth casting a dim green light around you. You can still see the road to the south''',
    'exits': {
      'south': 'road'
    }
  }
}