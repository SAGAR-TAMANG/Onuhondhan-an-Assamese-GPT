from django.shortcuts import render, HttpResponse
from dotenv import load_dotenv
import os, random
load_dotenv()

cards = [
  "অসমৰ বিখ্যাত পৰ্যটন স্থানসমূহ #কি কি?",
  "বিহু উৎসৱটো #কি?",
  "এটা জনপ্ৰিয় অসমীয়া গীতৰ পৰামৰ্শ #দিয়ক।",
  "অসমৰ ইতিহাস #চমুকৈ বুজাই দিব পৰা নেকি?",
  "জনপ্ৰিয় অসমীয়া ইউটিউব চেনেল কেইখন #কি?",
  "কাজিৰঙা ৰাষ্ট্ৰীয় উদ্যানৰ গুৰুত্ব #কি?",
  "অসমৰ প্ৰাকৃতিক সৌন্দৰ্যৰ কথা #ক’বচোন।",
  "অসমীয়া লোককথাৰ কাহিনী #এটা ক’ব পাৰিবা নে?",
  "বিখ্যাত অসমীয়া লেখক #কোন কেইজনমান আছে?",
  "অসমৰ সাংস্কৃতিক প্ৰতীক #কি কি?"
  "অসমীয়া গীতৰ ইতিহাস #কি?",
  "অসমৰ সংস্কৃতিৰ মূল উপাদানবোৰ #কি কি?",
  "অসমীয়া সাহিত্যৰ বিখ্যাত গ্ৰন্থসমূহ #কিহঁত?",
  "অসমৰ পৰা বিশ্বমঞ্চত বিখ্যাত অসমীয়া ব্যক্তিত্ব #কোন?",
  "অসমৰ চাহ বাগিচাৰ ইতিহাস #কি?",
  "অসমীয়া পৰম্পৰাগত খাদ্যসমূহ #কি কি?",
  "অসমীয়া নাটক আৰু সংস্কৃতিৰ ইতিহাস #কি?",
  "অসমৰ পৰ্যটন ক্ষেত্ৰৰ বিকাশ #কেনেকৈ হৈছে?",
  "অসমৰ চিৰস্থায়ী সমস্যা আৰু সমাধান #কি কি?",
  "অসমৰ ইতিহাসত গুৰুত্বপূৰ্ণ ঘটনা #কি কি?"
]

def index(request):
  return render(request, 'index.html')

def app(request):
  cards_bold, cards_normal = card_choser()

  context = {
     'cards_bold': cards_bold,
     'cards_normal': cards_normal,
     'zipped': zip(cards_bold, cards_normal)
  }

  return render(request, 'app.html', context=context)

def card_choser():
  chosen = random.sample(cards, 4)

  bold_texts = []
  normal_texts = []

  for card in chosen:
    parts = card.split("#")
    bold_texts.append(parts[0])
    normal_texts.append(parts[1])

  return bold_texts, normal_texts

  print('\n\nFINAL \n\n')

  print("Complete response:", response_text)
  
  return render(request, 'app.html')

def handler500(request):
  return render(request, 'handler500.html', status=500)

def handler404(request, exception):
  return render(request, 'handler404.html', status=404) 