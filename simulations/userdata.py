import os, requests

random_users = {
    "names": [
        {"fname": "Jane", "lname": "Smith"},
        {"fname": "Michael", "lname": "Johnson"},
        {"fname": "Emily", "lname": "Williams"},
        {"fname": "David", "lname": "Brown"},
        {"fname": "Sophia", "lname": "Jones"},
        {"fname": "Matthew", "lname": "Davis"},
        {"fname": "Olivia", "lname": "Miller"},
        {"fname": "Christopher", "lname": "Taylor"},
        {"fname": "Emma", "lname": "Anderson"},
        {"fname": "Andrew", "lname": "Thomas"},
        {"fname": "Ava", "lname": "White"},
        {"fname": "William", "lname": "Moore"},
        {"fname": "Madison", "lname": "Hill"},
        {"fname": "Daniel", "lname": "Walker"},
        {"fname": "Sofia", "lname": "Carter"},
        {"fname": "Liam", "lname": "Wright"},
        {"fname": "Abigail", "lname": "Martin"},
        {"fname": "Ethan", "lname": "Harris"},
        {"fname": "Mia", "lname": "Clark"},
        {"fname": "Joseph", "lname": "Lewis"},
        {"fname": "Isabella", "lname": "Hall"},
        {"fname": "James", "lname": "Allen"},
        {"fname": "Grace", "lname": "Young"},
        {"fname": "Benjamin", "lname": "Scott"},
        {"fname": "Avery", "lname": "Adams"},
        {"fname": "Logan", "lname": "Nelson"},
        {"fname": "Chloe", "lname": "Baker"},
        {"fname": "Joshua", "lname": "Harrison"},
        {"fname": "Addison", "lname": "Henderson"},
        {"fname": "Nicholas", "lname": "Perry"},
        {"fname": "Natalie", "lname": "Barnes"},
        {"fname": "Caleb", "lname": "Roberts"},
        {"fname": "Lily", "lname": "Cooper"},
        {"fname": "Alexander", "lname": "Morgan"},
        {"fname": "Hannah", "lname": "Graham"},
        {"fname": "Ryan", "lname": "Stewart"},
        {"fname": "Ella", "lname": "Cooper"},
        {"fname": "Jackson", "lname": "Cruz"},
        {"fname": "Aria", "lname": "Perez"},
        {"fname": "Nathan", "lname": "Simmons"},
        {"fname": "Aubrey", "lname": "Fisher"},
        {"fname": "Samuel", "lname": "Lopez"},
        {"fname": "Scarlett", "lname": "Bryant"},
        {"fname": "Dylan", "lname": "Foster"},
        {"fname": "Ellie", "lname": "Gomez"},
        {"fname": "Owen", "lname": "Hernandez"},
        {"fname": "Brooklyn", "lname": "Jordan"},
        {"fname": "Gabriel", "lname": "Ross"},
        {"fname": "Peyton", "lname": "Ward"},
        {"fname": "Isaac", "lname": "Patterson"},
        {"fname": "Mila", "lname": "Bryant"},
        {"fname": "Wyatt", "lname": "Reed"},
        {"fname": "Leah", "lname": "Phillips"},
        {"fname": "Henry", "lname": "Evans"},
        {"fname": "Victoria", "lname": "Mitchell"},
        {"fname": "Elijah", "lname": "Hayes"},
        {"fname": "Zoe", "lname": "Wheeler"},
        {"fname": "Aiden", "lname": "Harper"},
        {"fname": "Gabriella", "lname": "Myers"},
        {"fname": "Grayson", "lname": "Cole"},
        {"fname": "Claire", "lname": "Watson"},
        {"fname": "Julian", "lname": "Gordon"},
        {"fname": "Layla", "lname": "Walters"},
        {"fname": "Hunter", "lname": "Murray"},
        {"fname": "Nora", "lname": "Jenkins"},
        {"fname": "Lincoln", "lname": "Perkins"},
        {"fname": "Stella", "lname": "Hudson"},
        {"fname": "Gavin", "lname": "Fleming"},
        {"fname": "Lillian", "lname": "Bishop"},
        {"fname": "Luke", "lname": "Davidson"},
        {"fname": "Kylie", "lname": "Gilbert"},
        {"fname": "Jack", "lname": "Holt"},
        {"fname": "Sarah", "lname": "Bass"},
        {"fname": "Carter", "lname": "McCarthy"},
        {"fname": "Aaliyah", "lname": "Mason"},
        {"fname": "Theodore", "lname": "Benson"},
        {"fname": "Violet", "lname": "Sullivan"},
        {"fname": "Nicholas", "lname": "Morrison"},
        {"fname": "Adeline", "lname": "Pierce"},
        {"fname": "Mason", "lname": "Wells"},
        {"fname": "Aurora", "lname": "Gardner"},
        {"fname": "Evan", "lname": "Austin"},
        {"fname": "Hazel", "lname": "Saunders"},
        {"fname": "Max", "lname": "Ferguson"},
        {"fname": "Alice", "lname": "Hardy"},
        {"fname": "Parker", "lname": "Wong"},
        {"fname": "Avery", "lname": "Lincoln"},
        {"fname": "Nolan", "lname": "Wang"},
        {"fname": "Savannah", "lname": "Richards"},
        {"fname": "Zachary", "lname": "Hancock"},
        {"fname": "Alyssa", "lname": "Kim"},
        {"fname": "Christian", "lname": "Chen"},
        {"fname": "Skylar", "lname": "Wu"},
        {"fname": "Cameron", "lname": "Chang"},
        {"fname": "Hailey", "lname": "Yang"},
        {"fname": "Landon", "lname": "Woods"},
        {"fname": "Penelope", "lname": "Burke"},
        {"fname": "Cole", "lname": "Hartman"},
        {"fname": "Ruby", "lname": "Porter"},
        {"fname": "Sebastian", "lname": "Mendoza"},
        {"fname": "Luna", "lname": "Casey"},
        {"fname": "Bryson", "lname": "Sheppard"},
        {"fname": "Nova", "lname": "Thornton"},
        {"fname": "Jaxon", "lname": "Gibbs"},
        {"fname": "Adriana", "lname": "Lynch"},
        {"fname": "Brayden", "lname": "Keller"},
        {"fname": "Eva", "lname": "Delgado"},
        {"fname": "Dominic", "lname": "Montgomery"},
        {"fname": "Sadie", "lname": "Hodge"},
        {"fname": "Oscar", "lname": "Lawson"},
        {"fname": "Athena", "lname": "Barrera"},
        {"fname": "Colton", "lname": "Floyd"},
        {"fname": "Ariana", "lname": "Mills"},
        {"fname": "Harrison", "lname": "Kirk"},
        {"fname": "Ivy", "lname": "Santos"},
        {"fname": "Everett", "lname": "Gaines"},
        {"fname": "Maya", "lname": "Black"},
        {"fname": "Brantley", "lname": "Vasquez"},
        {"fname": "Isaiah", "lname": "Flynn"},
        {"fname": "Elise", "lname": "Hodge"},
        {"fname": "Gideon", "lname": "Lam"},
        {"fname": "Liliana", "lname": "Huang"},
        {"fname": "Kaden", "lname": "Benson"},
        {"fname": "Harper", "lname": "Haley"},
        {"fname": "Ryder", "lname": "Mathews"},
        {"fname": "Evelyn", "lname": "Mann"},
        {"fname": "Axel", "lname": "Hooper"},
        {"fname": "Aria", "lname": "Morse"},
        {"fname": "Kai", "lname": "Farrell"},
        {"fname": "Lila", "lname": "Fleming"},
        {"fname": "Knox", "lname": "Walters"},
        {"fname": "Mackenzie", "lname": "Dougherty"},
        {"fname": "Jace", "lname": "Oneal"},
        {"fname": "Alaina", "lname": "Huang"},
        {"fname": "Blake", "lname": "Jennings"},
        {"fname": "Gianna", "lname": "Beasley"},
        {"fname": "Easton", "lname": "Thornton"},
        {"fname": "Nova", "lname": "Riley"},
        {"fname": "Xavier", "lname": "Kane"},
        {"fname": "Alexis", "lname": "Galloway"},
        {"fname": "Carter", "lname": "Boyd"},
        {"fname": "Aubree", "lname": "Salazar"},
        {"fname": "Damian", "lname": "Cantu"},
        {"fname": "Emery", "lname": "Webb"}
    ],
    "usernames": [
        "alpha123",
        "beta456",
        "gamma789",
        "delta234",
        "epsilon567",
        "zeta890",
        "eta123",
        "theta456",
        "iota789",
        "kappa234",
        "lambda567",
        "mu890",
        "nu123",
        "xi456",
        "omicron789",
        "pi234",
        "rho567",
        "sigma890",
        "tau123",
        "upsilon456",
        "phi789",
        "chi234",
        "psi567",
        "omega890",
        "user123",
        "random456",
        "username789",
        "example234",
        "test567",
        "user1",
        "user2",
        "user3",
        "user4",
        "user5",
        "user6",
        "user7",
        "user8",
        "user9",
        "user10",
        "user11",
        "user12",
        "user13",
        "user14",
        "user15",
        "user16",
        "user17",
        "user18",
        "user19",
        "user20",
        "user21",
        "user22",
        "user23",
        "user24",
        "user25",
        "user26",
        "user27",
        "user28",
        "user29",
        "user30",
        "user31",
        "user32",
        "user33",
        "user34",
        "user35",
        "user36",
        "user37",
        "user38",
        "user39",
        "user40",
        "user41",
        "user42",
        "user43",
        "user44",
        "user45",
        "user46",
        "user47",
        "user48",
        "user49",
        "user50",
        "user51",
        "user52",
        "user53",
        "user54",
        "user55",
        "user56",
        "user57",
        "user58",
        "user59",
        "user60",
        "user61",
        "user62",
        "user63",
        "user64",
        "user65",
        "user66",
        "user67",
        "user68",
        "user69",
        "user70",
        "user71",
        "user72",
        "user73",
        "user74",
        "user75",
        "user76",
        "user77",
        "user78",
        "user79",
        "user80",
        "user81",
        "user82",
        "user83",
        "user84",
        "user85",
        "user86",
        "user87",
        "user88",
        "user89",
        "user90",
        "user91",
        "user92",
        "user93",
        "user94",
        "user95",
        "user96",
        "user97",
        "user98",
        "user99",
        "user100",
        "user101",
        "user102",
        "user103",
        "user104",
        "user105",
        "user106",
        "user107",
        "user108",
        "user109",
        "user110",
        "user111",
        "user112",
        "user113",
        "user114",
        "user115"
    ]
}



def generate(num):
    if(num<1): num = 1
    if(num>146): num = 146
    count = 0
    for x in range(0, num):
        new_user = {
        'username' : random_users["usernames"][x],
        'email' : random_users["usernames"][x] + "@example.com",
        'password' : "$2b$12$F1vR9Qtasr49FSHOdWP3LOecAC4JBPyiiIP8DI/MvRuW9JMpPHNZi",
        'fname' : random_users["names"][x]["fname"],
        'lname' : random_users["names"][x]["lname"],
        'role' : 'Standard'
        }
        r = requests.post(os.getenv('DB_URL') + "/users", json=new_user)
        if(r.status_code == 201): count += 1
    return count