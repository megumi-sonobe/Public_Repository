from django.core.management.base import BaseCommand, CommandParser


class Command(BaseCommand):
    help='ユーザー情報を表示するバッチです'
    
    def add_arguments(self, parser):
        parser.add_argument('name',type=str)#1引数
        parser.add_argument('age',type=int,help='名前')#2引数
        parser.add_argument('--birthday',default='2020-01-01')
        parser.add_argument('three_words',nargs=3)
        parser.add_argument('--active',action='store_true')
        parser.add_argument('--color',choices=['Blue','Red','Yellow'])
        
    def handle(self, *args,**options):
        name = options['name']
        age = options['age']
        birthday = options['birthday']
        three_words=options['three_words']
        active = options['active']
        
        print(type(age))
        print(
            f'name = {name},age = {age},birthday = {birthday},three_words={three_words}'
            )
        print(active)
        color = options['color']
        if color =='Blue':
            print('青')
        elif color =='Red':
            print('赤')
        elif color == 'Yellow':
            print('黄')
            
            
            
        
     
        