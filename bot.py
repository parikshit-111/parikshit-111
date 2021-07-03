import discord
from discord.ext import commands
import csv
from time import sleep
import urllib.request, json
import requests
import pandas as pd
from datetime import date
from termcolor import colored 
import emoji


client = commands.Bot(command_prefix=">")


rules=["1. To get the details of your district, you need to call >pin function with the pincode. Eg, >pin 785001",
       "2. Do not pass any String as a parameter.",
       "3. Please adhere to the Terms and Conditions of Discord",
       "4. Bot is still on development phase. If you are facing any issues, please contact pbarua111.official@gmail.com",
       "5. Get vaccinated ASAP"]


@client.event
async def on_ready():
    print("Bot is ready")
    
@client.command(aliases=["Hi","Yo","hi","yo","ay","sup","Sup","heyy","hey","heyyy"])
async def hello(ctx):
    await ctx.send("Hey")
    await ctx.send("It's me! cowimo \U0001F489")
    await ctx.send("Type '>rule 0' to know more about me")
    await ctx.send(emoji.emojize(" :thumbs_up:"))

@client.command(aliases=["rules","support","cohelp"])
async def rule(ctx,*,number):
    if number=='0':
        for x in sex_rules:
            await ctx.send(x)
    else:
        if number.isdigit() and int(number)<=len(rules):
            await ctx.send(sex_rules[int(number)-1])
        else:
            val="Number is not within range"
            await ctx.send(val)

@client.command(aliases=["pincode"])
async def pin(ctx,*,pincode):
    get_output=get_vaccination_stats(pincode)
    for i in get_output:
        await ctx.send(i)


@client.command(aliases=["conews"])
async def news(ctx):
        await ctx.send("https://api.cowin.gov.in")

def get_vaccination_stats(pincode):
    #Storing all Indian States & UT details into dictionary 
    indian_states={1:"Andaman and Nicobar Islands",2:"Andhra Pradesh",
     3:"Arunachal Pradesh",
     4:"Assam",
     5:"Bihar",
     6:"Chandigarh",
     7:"Chhattisgarh",
     8:"Dadra and Nagar Haveli",
     9:"Delhi",
    10:"Goa",
    11:"Gujarat",
    12:"Haryana",
    13:"Himachal Pradesh",
    14:"Jammu and Kashmir",
    15:"Jharkhand",
    16:"Karnataka",
    17:"Kerala",
    18:"Ladakh",
    19:"Lakshadweep",
    20:"Madhya Pradesh",
    21:"Maharashtra",
    22:"Manipur",
    23:"Meghalaya",
    24:"Mizoram",
    25:"Nagaland",
    26:"Odisha",
    27:"Puducherry",
    28:"Punjab",
    29:"Rajasthan",
    30:"Sikkim",
    31:"Tamil Nadu",
    32:"Telangana",
    33:"Tripura",
    34:"Uttar Pradesh",
    35:"Uttarakhand",
    36:"West Bengal",
    37:"Daman and Diu"}
    
    #Storing all Indian district details into dictionary
    State_wise={
                                         "Andaman and Nicobar Islands": {
                                                                              "3": "Nicobar",
                                                                              "1": "North and Middle Andaman",
                                                                              "2": "South Andaman"
                                         },
                                         "Andhra Pradesh": {
                                                                              "9": "Anantapur",
                                                                              "10": "Chittoor",
                                                                              "11": "East Godavari",
                                                                              "5": "Guntur",
                                                                              "4": "Krishna",
                                                                              "7": "Kurnool",
                                                                              "12": "Prakasam",
                                                                              "13": "Sri Potti Sriramulu Nellore",
                                                                              "14": "Srikakulam",
                                                                              "8": "Visakhapatnam",
                                                                              "15": "Vizianagaram",
                                                                              "16": "West Godavari",
                                                                              "6": "YSR District, Kadapa (Cuddapah)"
                                         },
                                         "Arunachal Pradesh": {
                                                                              "22": "Anjaw",
                                                                              "20": "Changlang",
                                                                              "25": "Dibang Valley",
                                                                              "23": "East Kameng",
                                                                              "42": "East Siang",
                                                                              "17": "Itanagar Capital Complex",
                                                                              "24": "Kamle",
                                                                              "27": "Kra Daadi",
                                                                              "21": "Kurung Kumey",
                                                                              "33": "Lepa Rada",
                                                                              "29": "Lohit",
                                                                              "40": "Longding",
                                                                              "31": "Lower Dibang Valley",
                                                                              "18": "Lower Siang",
                                                                              "32": "Lower Subansiri",
                                                                              "36": "Namsai",
                                                                              "19": "Pakke Kessang",
                                                                              "39": "Papum Pare",
                                                                              "35": "Shi Yomi",
                                                                              "37": "Siang",
                                                                              "30": "Tawang",
                                                                              "26": "Tirap",
                                                                              "34": "Upper Siang",
                                                                              "41": "Upper Subansiri",
                                                                              "28": "West Kameng",
                                                                              "38": "West Siang"
                                         },
                                         "Assam": {
                                                                              "46": "Baksa",
                                                                              "47": "Barpeta",
                                                                              "765": "Biswanath",
                                                                              "57": "Bongaigaon",
                                                                              "66": "Cachar",
                                                                              "766": "Charaideo",
                                                                              "58": "Chirang",
                                                                              "48": "Darrang",
                                                                              "62": "Dhemaji",
                                                                              "59": "Dhubri",
                                                                              "43": "Dibrugarh",
                                                                              "67": "Dima Hasao",
                                                                              "60": "Goalpara",
                                                                              "53": "Golaghat",
                                                                              "68": "Hailakandi",
                                                                              "764": "Hojai",
                                                                              "54": "Jorhat",
                                                                              "49": "Kamrup Metropolitan",
                                                                              "50": "Kamrup Rural",
                                                                              "51": "Karbi-Anglong",
                                                                              "69": "Karimganj",
                                                                              "61": "Kokrajhar",
                                                                              "63": "Lakhimpur",
                                                                              "767": "Majuli",
                                                                              "55": "Morigaon",
                                                                              "56": "Nagaon",
                                                                              "52": "Nalbari",
                                                                              "44": "Sivasagar",
                                                                              "64": "Sonitpur",
                                                                              "768": "South Salmara Mankachar",
                                                                              "45": "Tinsukia",
                                                                              "65": "Udalguri",
                                                                              "769": "West Karbi Anglong"
                                         },
                                         "Bihar": {
                                                                              "74": "Araria",
                                                                              "78": "Arwal",
                                                                              "77": "Aurangabad",
                                                                              "83": "Banka",
                                                                              "98": "Begusarai",
                                                                              "82": "Bhagalpur",
                                                                              "99": "Bhojpur",
                                                                              "100": "Buxar",
                                                                              "94": "Darbhanga",
                                                                              "105": "East Champaran",
                                                                              "79": "Gaya",
                                                                              "104": "Gopalganj",
                                                                              "107": "Jamui",
                                                                              "91": "Jehanabad",
                                                                              "80": "Kaimur",
                                                                              "75": "Katihar",
                                                                              "101": "Khagaria",
                                                                              "76": "Kishanganj",
                                                                              "84": "Lakhisarai",
                                                                              "70": "Madhepura",
                                                                              "95": "Madhubani",
                                                                              "85": "Munger",
                                                                              "86": "Muzaffarpur",
                                                                              "90": "Nalanda",
                                                                              "92": "Nawada",
                                                                              "97": "Patna",
                                                                              "73": "Purnia",
                                                                              "81": "Rohtas",
                                                                              "71": "Saharsa",
                                                                              "96": "Samastipur",
                                                                              "102": "Saran",
                                                                              "93": "Sheikhpura",
                                                                              "87": "Sheohar",
                                                                              "88": "Sitamarhi",
                                                                              "103": "Siwan",
                                                                              "72": "Supaul",
                                                                              "89": "Vaishali",
                                                                              "106": "West Champaran"
                                         },
                                         "Chandigarh": {
                                                                              "108": "Chandigarh"
                                         },
                                         "Chhattisgarh": {
                                                                              "110": "Balod",
                                                                              "111": "Baloda bazar",
                                                                              "112": "Balrampur",
                                                                              "113": "Bastar",
                                                                              "114": "Bemetara",
                                                                              "115": "Bijapur",
                                                                              "116": "Bilaspur",
                                                                              "117": "Dantewada",
                                                                              "118": "Dhamtari",
                                                                              "119": "Durg",
                                                                              "120": "Gariaband",
                                                                              "136": "Gaurela Pendra Marwahi ",
                                                                              "121": "Janjgir-Champa",
                                                                              "122": "Jashpur",
                                                                              "123": "Kanker",
                                                                              "135": "Kawardha",
                                                                              "124": "Kondagaon",
                                                                              "125": "Korba",
                                                                              "126": "Koriya",
                                                                              "127": "Mahasamund",
                                                                              "128": "Mungeli",
                                                                              "129": "Narayanpur",
                                                                              "130": "Raigarh",
                                                                              "109": "Raipur",
                                                                              "131": "Rajnandgaon",
                                                                              "132": "Sukma",
                                                                              "133": "Surajpur",
                                                                              "134": "Surguja"
                                         },
                                         "Dadra and Nagar Haveli": {
                                                                              "137": "Dadra and Nagar Haveli"
                                         },
                                         "Delhi": {
                                                                              "141": "Central Delhi",
                                                                              "145": "East Delhi",
                                                                              "140": "New Delhi",
                                                                              "146": "North Delhi",
                                                                              "147": "North East Delhi",
                                                                              "143": "North West Delhi",
                                                                              "148": "Shahdara",
                                                                              "149": "South Delhi",
                                                                              "144": "South East Delhi",
                                                                              "150": "South West Delhi",
                                                                              "142": "West Delhi"
                                         },
                                         "Goa": {
                                                                              "151": "North Goa",
                                                                              "152": "South Goa"
                                         },
                                         "Gujarat": {
                                                                              "154": "Ahmedabad",
                                                                              "770": "Ahmedabad Corporation",
                                                                              "174": "Amreli",
                                                                              "179": "Anand",
                                                                              "158": "Aravalli",
                                                                              "159": "Banaskantha",
                                                                              "180": "Bharuch",
                                                                              "175": "Bhavnagar",
                                                                              "771": "Bhavnagar Corporation",
                                                                              "176": "Botad",
                                                                              "181": "Chhotaudepur",
                                                                              "182": "Dahod",
                                                                              "163": "Dang",
                                                                              "168": "Devbhumi Dwaraka",
                                                                              "153": "Gandhinagar",
                                                                              "772": "Gandhinagar Corporation",
                                                                              "177": "Gir Somnath",
                                                                              "169": "Jamnagar",
                                                                              "773": "Jamnagar Corporation",
                                                                              "178": "Junagadh",
                                                                              "774": "Junagadh Corporation",
                                                                              "156": "Kheda",
                                                                              "170": "Kutch",
                                                                              "183": "Mahisagar",
                                                                              "160": "Mehsana",
                                                                              "171": "Morbi",
                                                                              "184": "Narmada",
                                                                              "164": "Navsari",
                                                                              "185": "Panchmahal",
                                                                              "161": "Patan",
                                                                              "172": "Porbandar",
                                                                              "173": "Rajkot",
                                                                              "775": "Rajkot Corporation",
                                                                              "162": "Sabarkantha",
                                                                              "165": "Surat",
                                                                              "776": "Surat Corporation",
                                                                              "157": "Surendranagar",
                                                                              "166": "Tapi",
                                                                              "155": "Vadodara",
                                                                              "777": "Vadodara Corporation",
                                                                              "167": "Valsad"
                                         },
                                         "Haryana": {
                                                                              "193": "Ambala",
                                                                              "200": "Bhiwani",
                                                                              "201": "Charkhi Dadri",
                                                                              "199": "Faridabad",
                                                                              "196": "Fatehabad",
                                                                              "188": "Gurgaon",
                                                                              "191": "Hisar",
                                                                              "189": "Jhajjar",
                                                                              "204": "Jind",
                                                                              "190": "Kaithal",
                                                                              "203": "Karnal",
                                                                              "186": "Kurukshetra",
                                                                              "206": "Mahendragarh",
                                                                              "205": "Nuh",
                                                                              "207": "Palwal",
                                                                              "187": "Panchkula",
                                                                              "195": "Panipat",
                                                                              "202": "Rewari",
                                                                              "192": "Rohtak",
                                                                              "194": "Sirsa",
                                                                              "198": "Sonipat",
                                                                              "197": "Yamunanagar"
                                         },
                                         "Himachal Pradesh": {
                                                                              "219": "Bilaspur",
                                                                              "214": "Chamba",
                                                                              "217": "Hamirpur",
                                                                              "213": "Kangra",
                                                                              "216": "Kinnaur",
                                                                              "211": "Kullu",
                                                                              "210": "Lahaul Spiti",
                                                                              "215": "Mandi",
                                                                              "208": "Shimla",
                                                                              "212": "Sirmaur",
                                                                              "209": "Solan",
                                                                              "218": "Una"
                                         },
                                         "Jammu and Kashmir": {
                                                                              "224": "Anantnag",
                                                                              "223": "Bandipore",
                                                                              "225": "Baramulla",
                                                                              "229": "Budgam",
                                                                              "232": "Doda",
                                                                              "228": "Ganderbal",
                                                                              "230": "Jammu",
                                                                              "234": "Kathua",
                                                                              "231": "Kishtwar",
                                                                              "221": "Kulgam",
                                                                              "226": "Kupwara",
                                                                              "238": "Poonch",
                                                                              "227": "Pulwama",
                                                                              "237": "Rajouri",
                                                                              "235": "Ramban",
                                                                              "239": "Reasi",
                                                                              "236": "Samba",
                                                                              "222": "Shopian",
                                                                              "220": "Srinagar",
                                                                              "233": "Udhampur"
                                         },
                                         "Jharkhand": {
                                                                              "242": "Bokaro",
                                                                              "245": "Chatra",
                                                                              "253": "Deoghar",
                                                                              "257": "Dhanbad",
                                                                              "258": "Dumka",
                                                                              "247": "East Singhbhum",
                                                                              "243": "Garhwa",
                                                                              "256": "Giridih",
                                                                              "262": "Godda",
                                                                              "251": "Gumla",
                                                                              "255": "Hazaribagh",
                                                                              "259": "Jamtara",
                                                                              "252": "Khunti",
                                                                              "241": "Koderma",
                                                                              "244": "Latehar",
                                                                              "250": "Lohardaga",
                                                                              "261": "Pakur",
                                                                              "246": "Palamu",
                                                                              "254": "Ramgarh",
                                                                              "240": "Ranchi",
                                                                              "260": "Sahebganj",
                                                                              "248": "Seraikela Kharsawan",
                                                                              "249": "Simdega",
                                                                              "263": "West Singhbhum"
                                         },
                                         "Karnataka": {
                                                                              "270": "Bagalkot",
                                                                              "276": "Bangalore Rural",
                                                                              "265": "Bangalore Urban",
                                                                              "294": "BBMP",
                                                                              "264": "Belgaum",
                                                                              "274": "Bellary",
                                                                              "272": "Bidar",
                                                                              "271": "Chamarajanagar",
                                                                              "273": "Chikamagalur",
                                                                              "291": "Chikkaballapur",
                                                                              "268": "Chitradurga",
                                                                              "269": "Dakshina Kannada",
                                                                              "275": "Davanagere",
                                                                              "278": "Dharwad",
                                                                              "280": "Gadag",
                                                                              "267": "Gulbarga",
                                                                              "289": "Hassan",
                                                                              "279": "Haveri",
                                                                              "283": "Kodagu",
                                                                              "277": "Kolar",
                                                                              "282": "Koppal",
                                                                              "290": "Mandya",
                                                                              "266": "Mysore",
                                                                              "284": "Raichur",
                                                                              "292": "Ramanagara",
                                                                              "287": "Shimoga",
                                                                              "288": "Tumkur",
                                                                              "286": "Udupi",
                                                                              "281": "Uttar Kannada",
                                                                              "293": "Vijayapura",
                                                                              "285": "Yadgir"
                                         },
                                         "Kerala": {
                                                                              "301": "Alappuzha",
                                                                              "307": "Ernakulam",
                                                                              "306": "Idukki",
                                                                              "297": "Kannur",
                                                                              "295": "Kasaragod",
                                                                              "298": "Kollam",
                                                                              "304": "Kottayam",
                                                                              "305": "Kozhikode",
                                                                              "302": "Malappuram",
                                                                              "308": "Palakkad",
                                                                              "300": "Pathanamthitta",
                                                                              "296": "Thiruvananthapuram",
                                                                              "303": "Thrissur",
                                                                              "299": "Wayanad"
                                         },
                                         "Ladakh": {
                                                                              "309": "Kargil",
                                                                              "310": "Leh"
                                         },
                                         "Lakshadweep": {
                                                                              "796": "Agatti Island",
                                                                              "311": "Lakshadweep"
                                         },
                                         "Madhya Pradesh": {
                                                                              "320": "Agar",
                                                                              "357": "Alirajpur",
                                                                              "334": "Anuppur",
                                                                              "354": "Ashoknagar",
                                                                              "338": "Balaghat",
                                                                              "343": "Barwani",
                                                                              "362": "Betul",
                                                                              "351": "Bhind",
                                                                              "312": "Bhopal",
                                                                              "342": "Burhanpur",
                                                                              "328": "Chhatarpur",
                                                                              "337": "Chhindwara",
                                                                              "327": "Damoh",
                                                                              "350": "Datia",
                                                                              "324": "Dewas",
                                                                              "341": "Dhar",
                                                                              "336": "Dindori",
                                                                              "348": "Guna",
                                                                              "313": "Gwalior",
                                                                              "361": "Harda",
                                                                              "360": "Hoshangabad",
                                                                              "314": "Indore",
                                                                              "315": "Jabalpur",
                                                                              "340": "Jhabua",
                                                                              "353": "Katni",
                                                                              "339": "Khandwa",
                                                                              "344": "Khargone",
                                                                              "335": "Mandla",
                                                                              "319": "Mandsaur",
                                                                              "347": "Morena",
                                                                              "352": "Narsinghpur",
                                                                              "323": "Neemuch",
                                                                              "326": "Panna",
                                                                              "359": "Raisen",
                                                                              "358": "Rajgarh",
                                                                              "322": "Ratlam",
                                                                              "316": "Rewa",
                                                                              "317": "Sagar",
                                                                              "333": "Satna",
                                                                              "356": "Sehore",
                                                                              "349": "Seoni",
                                                                              "332": "Shahdol",
                                                                              "321": "Shajapur",
                                                                              "346": "Sheopur",
                                                                              "345": "Shivpuri",
                                                                              "331": "Sidhi",
                                                                              "330": "Singrauli",
                                                                              "325": "Tikamgarh",
                                                                              "318": "Ujjain",
                                                                              "329": "Umaria",
                                                                              "355": "Vidisha"
                                         },
                                         "Maharashtra": {
                                                                              "391": "Ahmednagar",
                                                                              "364": "Akola",
                                                                              "366": "Amravati",
                                                                              "397": "Aurangabad ",
                                                                              "384": "Beed",
                                                                              "370": "Bhandara",
                                                                              "367": "Buldhana",
                                                                              "380": "Chandrapur",
                                                                              "388": "Dhule",
                                                                              "379": "Gadchiroli",
                                                                              "378": "Gondia",
                                                                              "386": "Hingoli",
                                                                              "390": "Jalgaon",
                                                                              "396": "Jalna",
                                                                              "371": "Kolhapur",
                                                                              "383": "Latur",
                                                                              "395": "Mumbai",
                                                                              "365": "Nagpur",
                                                                              "382": "Nanded",
                                                                              "387": "Nandurbar",
                                                                              "389": "Nashik",
                                                                              "381": "Osmanabad",
                                                                              "394": "Palghar",
                                                                              "385": "Parbhani",
                                                                              "363": "Pune",
                                                                              "393": "Raigad",
                                                                              "372": "Ratnagiri",
                                                                              "373": "Sangli",
                                                                              "376": "Satara",
                                                                              "374": "Sindhudurg",
                                                                              "375": "Solapur",
                                                                              "392": "Thane",
                                                                              "377": "Wardha",
                                                                              "369": "Washim",
                                                                              "368": "Yavatmal"
                                         },
                                         "Manipur": {
                                                                              "398": "Bishnupur",
                                                                              "399": "Chandel",
                                                                              "400": "Churachandpur",
                                                                              "401": "Imphal East",
                                                                              "402": "Imphal West",
                                                                              "410": "Jiribam",
                                                                              "413": "Kakching",
                                                                              "409": "Kamjong",
                                                                              "408": "Kangpokpi",
                                                                              "412": "Noney",
                                                                              "411": "Pherzawl",
                                                                              "403": "Senapati",
                                                                              "404": "Tamenglong",
                                                                              "407": "Tengnoupal",
                                                                              "405": "Thoubal",
                                                                              "406": "Ukhrul"
                                         },
                                         "Meghalaya": {
                                                                              "424": "East Garo Hills",
                                                                              "418": "East Jaintia Hills",
                                                                              "414": "East Khasi Hills",
                                                                              "423": "North Garo Hills",
                                                                              "417": "Ri-Bhoi",
                                                                              "421": "South Garo Hills",
                                                                              "422": "South West Garo Hills",
                                                                              "415": "South West Khasi Hills",
                                                                              "420": "West Garo Hills",
                                                                              "416": "West Jaintia Hills",
                                                                              "419": "West Khasi Hills"
                                         },
                                         "Mizoram": {
                                                                              "425": "Aizawl East",
                                                                              "426": "Aizawl West",
                                                                              "429": "Champhai",
                                                                              "428": "Kolasib",
                                                                              "432": "Lawngtlai",
                                                                              "431": "Lunglei",
                                                                              "427": "Mamit",
                                                                              "430": "Serchhip",
                                                                              "433": "Siaha"
                                         },
                                         "Nagaland": {
                                                                              "434": "Dimapur",
                                                                              "444": "Kiphire",
                                                                              "441": "Kohima",
                                                                              "438": "Longleng",
                                                                              "437": "Mokokchung",
                                                                              "439": "Mon",
                                                                              "435": "Peren",
                                                                              "443": "Phek",
                                                                              "440": "Tuensang",
                                                                              "436": "Wokha",
                                                                              "442": "Zunheboto"
                                         },
                                         "Odisha": {
                                                                              "445": "Angul",
                                                                              "448": "Balangir",
                                                                              "447": "Balasore",
                                                                              "472": "Bargarh",
                                                                              "454": "Bhadrak",
                                                                              "468": "Boudh",
                                                                              "457": "Cuttack",
                                                                              "473": "Deogarh",
                                                                              "458": "Dhenkanal",
                                                                              "467": "Gajapati",
                                                                              "449": "Ganjam",
                                                                              "459": "Jagatsinghpur",
                                                                              "460": "Jajpur",
                                                                              "474": "Jharsuguda",
                                                                              "464": "Kalahandi",
                                                                              "450": "Kandhamal",
                                                                              "461": "Kendrapara",
                                                                              "455": "Kendujhar",
                                                                              "446": "Khurda",
                                                                              "451": "Koraput",
                                                                              "469": "Malkangiri",
                                                                              "456": "Mayurbhanj",
                                                                              "470": "Nabarangpur",
                                                                              "462": "Nayagarh",
                                                                              "465": "Nuapada",
                                                                              "463": "Puri",
                                                                              "471": "Rayagada",
                                                                              "452": "Sambalpur",
                                                                              "466": "Subarnapur",
                                                                              "453": "Sundargarh"
                                         },
                                         "Puducherry": {
                                                                              "476": "Karaikal",
                                                                              "477": "Mahe",
                                                                              "475": "Puducherry",
                                                                              "478": "Yanam"
                                         },
                                         "Punjab": {
                                                                              "485": "Amritsar",
                                                                              "483": "Barnala",
                                                                              "493": "Bathinda",
                                                                              "499": "Faridkot",
                                                                              "484": "Fatehgarh Sahib",
                                                                              "487": "Fazilka",
                                                                              "480": "Ferozpur",
                                                                              "489": "Gurdaspur",
                                                                              "481": "Hoshiarpur",
                                                                              "492": "Jalandhar",
                                                                              "479": "Kapurthala",
                                                                              "488": "Ludhiana",
                                                                              "482": "Mansa",
                                                                              "491": "Moga",
                                                                              "486": "Pathankot",
                                                                              "494": "Patiala",
                                                                              "497": "Rup Nagar",
                                                                              "498": "Sangrur",
                                                                              "496": "SAS Nagar",
                                                                              "500": "SBS Nagar",
                                                                              "490": "Sri Muktsar Sahib",
                                                                              "495": "Tarn Taran"
                                         },
                                         "Rajasthan": {
                                                                              "507": "Ajmer",
                                                                              "512": "Alwar",
                                                                              "519": "Banswara",
                                                                              "516": "Baran",
                                                                              "528": "Barmer",
                                                                              "508": "Bharatpur",
                                                                              "523": "Bhilwara",
                                                                              "501": "Bikaner",
                                                                              "514": "Bundi",
                                                                              "521": "Chittorgarh",
                                                                              "530": "Churu",
                                                                              "511": "Dausa",
                                                                              "524": "Dholpur",
                                                                              "520": "Dungarpur",
                                                                              "517": "Hanumangarh",
                                                                              "505": "Jaipur I",
                                                                              "506": "Jaipur II",
                                                                              "527": "Jaisalmer",
                                                                              "533": "Jalore",
                                                                              "515": "Jhalawar",
                                                                              "510": "Jhunjhunu",
                                                                              "502": "Jodhpur",
                                                                              "525": "Karauli",
                                                                              "503": "Kota",
                                                                              "532": "Nagaur",
                                                                              "529": "Pali",
                                                                              "522": "Pratapgarh",
                                                                              "518": "Rajsamand",
                                                                              "534": "Sawai Madhopur",
                                                                              "513": "Sikar",
                                                                              "531": "Sirohi",
                                                                              "509": "Sri Ganganagar",
                                                                              "526": "Tonk",
                                                                              "504": "Udaipur"
                                         },
                                         "Sikkim": {
                                                                              "535": "East Sikkim",
                                                                              "537": "North Sikkim",
                                                                              "538": "South Sikkim",
                                                                              "536": "West Sikkim"
                                         },
                                         "Tamil Nadu": {
                                                                              "779": "Aranthangi",
                                                                              "555": "Ariyalur",
                                                                              "578": "Attur",
                                                                              "565": "Chengalpet",
                                                                              "571": "Chennai",
                                                                              "778": "Cheyyar",
                                                                              "539": "Coimbatore",
                                                                              "547": "Cuddalore",
                                                                              "566": "Dharmapuri",
                                                                              "556": "Dindigul",
                                                                              "563": "Erode",
                                                                              "552": "Kallakurichi",
                                                                              "557": "Kanchipuram",
                                                                              "544": "Kanyakumari",
                                                                              "559": "Karur",
                                                                              "780": "Kovilpatti",
                                                                              "562": "Krishnagiri",
                                                                              "540": "Madurai",
                                                                              "576": "Nagapattinam",
                                                                              "558": "Namakkal",
                                                                              "577": "Nilgiris",
                                                                              "564": "Palani",
                                                                              "573": "Paramakudi",
                                                                              "570": "Perambalur",
                                                                              "575": "Poonamallee",
                                                                              "546": "Pudukkottai",
                                                                              "567": "Ramanathapuram",
                                                                              "781": "Ranipet",
                                                                              "545": "Salem",
                                                                              "561": "Sivaganga",
                                                                              "580": "Sivakasi",
                                                                              "551": "Tenkasi",
                                                                              "541": "Thanjavur",
                                                                              "569": "Theni",
                                                                              "554": "Thoothukudi (Tuticorin)",
                                                                              "560": "Tiruchirappalli",
                                                                              "548": "Tirunelveli",
                                                                              "550": "Tirupattur",
                                                                              "568": "Tiruppur",
                                                                              "572": "Tiruvallur",
                                                                              "553": "Tiruvannamalai",
                                                                              "574": "Tiruvarur",
                                                                              "543": "Vellore",
                                                                              "542": "Viluppuram",
                                                                              "549": "Virudhunagar"
                                         },
                                         "Telangana": {
                                                                              "582": "Adilabad",
                                                                              "583": "Bhadradri Kothagudem",
                                                                              "581": "Hyderabad",
                                                                              "584": "Jagtial",
                                                                              "585": "Jangaon",
                                                                              "586": "Jayashankar Bhupalpally",
                                                                              "587": "Jogulamba Gadwal",
                                                                              "588": "Kamareddy",
                                                                              "589": "Karimnagar",
                                                                              "590": "Khammam",
                                                                              "591": "Kumuram Bheem",
                                                                              "592": "Mahabubabad",
                                                                              "593": "Mahabubnagar",
                                                                              "594": "Mancherial",
                                                                              "595": "Medak",
                                                                              "596": "Medchal",
                                                                              "612": "Mulugu",
                                                                              "597": "Nagarkurnool",
                                                                              "598": "Nalgonda",
                                                                              "613": "Narayanpet",
                                                                              "599": "Nirmal",
                                                                              "600": "Nizamabad",
                                                                              "601": "Peddapalli",
                                                                              "602": "Rajanna Sircilla",
                                                                              "603": "Rangareddy",
                                                                              "604": "Sangareddy",
                                                                              "605": "Siddipet",
                                                                              "606": "Suryapet",
                                                                              "607": "Vikarabad",
                                                                              "608": "Wanaparthy",
                                                                              "609": "Warangal(Rural)",
                                                                              "610": "Warangal(Urban)",
                                                                              "611": "Yadadri Bhuvanagiri"
                                         },
                                         "Tripura": {
                                                                              "614": "Dhalai",
                                                                              "615": "Gomati",
                                                                              "616": "Khowai",
                                                                              "617": "North Tripura",
                                                                              "618": "Sepahijala",
                                                                              "619": "South Tripura",
                                                                              "620": "Unakoti",
                                                                              "621": "West Tripura"
                                         },
                                         "Uttar Pradesh": {
                                                                              "622": "Agra",
                                                                              "623": "Aligarh",
                                                                              "625": "Ambedkar Nagar",
                                                                              "626": "Amethi",
                                                                              "627": "Amroha",
                                                                              "628": "Auraiya",
                                                                              "646": "Ayodhya",
                                                                              "629": "Azamgarh",
                                                                              "630": "Badaun",
                                                                              "631": "Baghpat",
                                                                              "632": "Bahraich",
                                                                              "633": "Balarampur",
                                                                              "634": "Ballia",
                                                                              "635": "Banda",
                                                                              "636": "Barabanki",
                                                                              "637": "Bareilly",
                                                                              "638": "Basti",
                                                                              "687": "Bhadohi",
                                                                              "639": "Bijnour",
                                                                              "640": "Bulandshahr",
                                                                              "641": "Chandauli",
                                                                              "642": "Chitrakoot",
                                                                              "643": "Deoria",
                                                                              "644": "Etah",
                                                                              "645": "Etawah",
                                                                              "647": "Farrukhabad",
                                                                              "648": "Fatehpur",
                                                                              "649": "Firozabad",
                                                                              "650": "Gautam Buddha Nagar",
                                                                              "651": "Ghaziabad",
                                                                              "652": "Ghazipur",
                                                                              "653": "Gonda",
                                                                              "654": "Gorakhpur",
                                                                              "655": "Hamirpur",
                                                                              "656": "Hapur",
                                                                              "657": "Hardoi",
                                                                              "658": "Hathras",
                                                                              "659": "Jalaun",
                                                                              "660": "Jaunpur",
                                                                              "661": "Jhansi",
                                                                              "662": "Kannauj",
                                                                              "663": "Kanpur Dehat",
                                                                              "664": "Kanpur Nagar",
                                                                              "665": "Kasganj",
                                                                              "666": "Kaushambi",
                                                                              "667": "Kushinagar",
                                                                              "668": "Lakhimpur Kheri",
                                                                              "669": "Lalitpur",
                                                                              "670": "Lucknow",
                                                                              "671": "Maharajganj",
                                                                              "672": "Mahoba",
                                                                              "673": "Mainpuri",
                                                                              "674": "Mathura",
                                                                              "675": "Mau",
                                                                              "676": "Meerut",
                                                                              "677": "Mirzapur",
                                                                              "678": "Moradabad",
                                                                              "679": "Muzaffarnagar",
                                                                              "680": "Pilibhit",
                                                                              "682": "Pratapgarh",
                                                                              "624": "Prayagraj",
                                                                              "681": "Raebareli",
                                                                              "683": "Rampur",
                                                                              "684": "Saharanpur",
                                                                              "685": "Sambhal",
                                                                              "686": "Sant Kabir Nagar",
                                                                              "688": "Shahjahanpur",
                                                                              "689": "Shamli",
                                                                              "690": "Shravasti",
                                                                              "691": "Siddharthnagar",
                                                                              "692": "Sitapur",
                                                                              "693": "Sonbhadra",
                                                                              "694": "Sultanpur",
                                                                              "695": "Unnao",
                                                                              "696": "Varanasi"
                                         },
                                         "Uttarakhand": {
                                                                              "704": "Almora",
                                                                              "707": "Bageshwar",
                                                                              "699": "Chamoli",
                                                                              "708": "Champawat",
                                                                              "697": "Dehradun",
                                                                              "702": "Haridwar",
                                                                              "709": "Nainital",
                                                                              "698": "Pauri Garhwal",
                                                                              "706": "Pithoragarh",
                                                                              "700": "Rudraprayag",
                                                                              "701": "Tehri Garhwal",
                                                                              "705": "Udham Singh Nagar",
                                                                              "703": "Uttarkashi"
                                         },
                                         "West Bengal": {
                                                                              "710": "Alipurduar District",
                                                                              "711": "Bankura",
                                                                              "712": "Basirhat HD (North 24 Parganas)",
                                                                              "713": "Birbhum",
                                                                              "714": "Bishnupur HD (Bankura)",
                                                                              "715": "Cooch Behar",
                                                                              "783": "COOCHBEHAR",
                                                                              "716": "Dakshin Dinajpur",
                                                                              "717": "Darjeeling",
                                                                              "718": "Diamond Harbor HD (S 24 Parganas)",
                                                                              "719": "East Bardhaman",
                                                                              "720": "Hoogly",
                                                                              "721": "Howrah",
                                                                              "722": "Jalpaiguri",
                                                                              "723": "Jhargram",
                                                                              "724": "Kalimpong",
                                                                              "725": "Kolkata",
                                                                              "726": "Malda",
                                                                              "727": "Murshidabad",
                                                                              "728": "Nadia",
                                                                              "729": "Nandigram HD (East Medinipore)",
                                                                              "730": "North 24 Parganas",
                                                                              "731": "Paschim Medinipore",
                                                                              "732": "Purba Medinipore",
                                                                              "733": "Purulia",
                                                                              "734": "Rampurhat HD (Birbhum)",
                                                                              "735": "South 24 Parganas",
                                                                              "736": "Uttar Dinajpur",
                                                                              "737": "West Bardhaman"
                                         },
                                         "Daman and Diu": {
                                                                              "138": "Daman",
                                                                              "139": "Diu"
                                         }
    }
    
    df = pd.read_csv('D:\Programming\Python\convertcsv.csv')
    l_district=int(pincode)
    dataframe=df[['Sheet1/Pincode', 'Sheet1/District','Sheet1/State']]
    rslt_df = dataframe[dataframe['Sheet1/Pincode'] == l_district] 
    sorted = rslt_df.sort_values(['Sheet1/Pincode'], ascending = [True])
    dups = sorted.drop_duplicates(subset=['Sheet1/District'])
    
    
    state=''
    district=''
    
    my_pkg=[]
    
    try:
        package=dups.values[0]
        district=package[1]
        state=package[2]
    except IndexError:
        print("No Pincode Available. Please try again")
    
    
    if district.lower()=='Kamrup'.lower():
        district='Kamrup Metropolitan'
         
    
    state=state.title()
    
    
    
    state_id=''
    district_id=''
    
    for x,i in  indian_states.items():
        if state:
            if i.lower()==state.lower():
                state_id=x
    
                
    if state:
        my_pkg.append("State : {}".format(state))
        key_list=list(State_wise[state].keys())
        value_list=list(State_wise[state].values())
        for i,x in enumerate(value_list):
            value_list[i]=x.lower()
        try:
            district_id=key_list[value_list.index(district.lower())]
        except ValueError:
            pass
    
    if state_id:
        #print("State id of {} is {}".format(state,state_id))
        if district_id:
            my_pkg.append("District : {}".format(district))
            #print("District id of {} is {}\n".format(district,district_id))
        else:
            #print("District id is not available. Considering for whole {}\n".format(state))
            district_id='&'
            my_pkg.append("District not found. Considering for whole {}\n".format(state))
            
    else:
        #print("State id is not available. Considering for India")
        state_id='&'
        my_pkg.append("State not found.  Considering for India")
    
    today = date.today()
    
    url='https://api.cowin.gov.in/api/v1/reports/v2/getPublicReports?state_id={}&district_id={}&date={}'.format(state_id,district_id,today)
    val=requests.get(url).json()
    
    
    total_vaccination=val['topBlock']['vaccination']['total_doses']
    total_vaccination_male=val['topBlock']['vaccination']['male']
    total_vaccination_female=val['topBlock']['vaccination']['female']
    total_vaccination_covishield=val['topBlock']['vaccination']['covishield']
    total_vaccination_covaxin=val['topBlock']['vaccination']['covaxin']
    total_vaccination_dose1=val['topBlock']['vaccination']['tot_dose_1']
    total_vaccination_dose2=val['topBlock']['vaccination']['tot_dose_2']
    
    today_total_vaccination=val['topBlock']['vaccination']['today']
    today_total_vaccination_male=val['topBlock']['vaccination']['today_male']
    today_total_vaccination_female=val['topBlock']['vaccination']['today_female']
    today_total_vaccination_dose1=val['topBlock']['vaccination']['today_dose_one']
    today_total_vaccination_dose2=val['topBlock']['vaccination']['today_dose_two']
    
    
    pkg='Total vaccination : {} \n'.format(total_vaccination)+'Total vaccination Male : {} \n'.format(total_vaccination_male)+'Total vaccination Female : {} \n'.format(total_vaccination_female)+'Total covishield shots : {} \n'.format(total_vaccination_covishield)+'Total covaxin shots : {} \n'.format(total_vaccination_covaxin)+'Total Dose 1 : {} \n'.format(total_vaccination_dose1)+'Total Dose 2 : {} \n'.format(total_vaccination_dose2)+'Today Total vaccination : {} \n'.format(today_total_vaccination)+'Today Total vaccination Male : {} \n'.format(today_total_vaccination_male)+'Today Total vaccination Female : {} \n'.format(today_total_vaccination_female)+'Today Total vaccination Dose 1 : {} \n'.format(today_total_vaccination_dose1)+'Today Total vaccination Dose 1 : {} \n'.format(today_total_vaccination_dose1)+'Today Total vaccination Dose 2 : {} \n'.format(today_total_vaccination_dose2)
    #my_pkg.append('Total vaccination : {}'.format(total_vaccination))
    #my_pkg.append('Total vaccination Male : {}'.format(total_vaccination_male))
    #my_pkg.append('Total vaccination Female : {}'.format(total_vaccination_female))
    #my_pkg.append('Total covishield shots : {}'.format(total_vaccination_covishield))
    #my_pkg.append('Total covaxin shots : {}'.format(total_vaccination_covaxin))
    #my_pkg.append('Total Dose 1 : {}'.format(total_vaccination_dose1))
    #my_pkg.append('Total Dose 2 : {}'.format(total_vaccination_dose2))
    #my_pkg.append('Today Total vaccination : {}'.format(today_total_vaccination))
    #my_pkg.append('Today Total vaccination Male : {}'.format(today_total_vaccination_male))
    #my_pkg.append('Today Total vaccination Female : {}'.format(today_total_vaccination_female))
    #my_pkg.append('Today Total vaccination Dose 1 : {}'.format(today_total_vaccination_dose1))
    #my_pkg.append('Today Total vaccination Dose 2 : {}'.format(today_total_vaccination_dose2))
    #my_pkg.append('\U0001F34C \U0001F351 \U0001F34B \U0001F919')
    my_pkg.append(pkg)
    
    return my_pkg
    #print('========================================================')
    #print('total_vaccination : ',total_vaccination)
    #print('total_vaccination_male : ',total_vaccination_male)
    #print('total_vaccination_female : ',total_vaccination_female)
    #print('total_vaccination_covishield : ',total_vaccination_covishield)
    #print('total_vaccination_covaxin : ',total_vaccination_covaxin)
    #print('total_vaccination_dose1 : ',total_vaccination_dose1)
    #print('total_vaccination_dose2 : ',total_vaccination_dose2)
    #print('today_total_vaccination : ',today_total_vaccination)
    #print('today_total_vaccination_male : ',today_total_vaccination_male)
    #print('today_total_vaccination_female : ',today_total_vaccination_female)
    #print('today_total_vaccination_dose1 : ',today_total_vaccination_dose1)
    #print('today_total_vaccination_dose2 : ',today_total_vaccination_dose2)
    #print('=======================================================')

    
client.run("ODUyNjAwMTI4MDMyMDc5OTIy.YMJLvw.BQOuD8dQpLHvnDxGEbPkzUZ_D6w")