import csv
import random
from pathlib import Path
from time import gmtime, strftime
from random import randrange
from datetime import timedelta
from datetime import datetime

number_of_rows_generated = 100
dataset_name = "befolkningsdata"
years = range(2020, 2021)
csv_file = Path(r"C:\BNJ\prosjektutvikling\GitHub\statisticsnorway\dapla-information-architecture\example_dataset\befolkningsdata").joinpath(dataset_name + ".csv")

minimum_date = datetime.strptime('1935-01-01', '%Y-%m-%d')
maximum_date = datetime.strptime('2020-01-01', '%Y-%m-%d')

kommune_liste = ["0301", "1101", "1103", "1106", "1108", "1111", "1112", "1114", "1119", "1120", "1121", "1122", "1124", "1127", "1130", "1133", "1134", "1135", "1144", "1145", "1146", "1149", "1151", "1160", "1505", "1506", "1507", "1511", "1514", "1515", "1516", "1517", "1520", "1525", "1528", "1531", "1532", "1535", "1539", "1547", "1554", "1557", "1560", "1563", "1566", "1573", "1576", "1577", "1578", "1579", "1804", "1806", "1811", "1812", "1813", "1815", "1816", "1818", "1820", "1822", "1824", "1825", "1826", "1827", "1828", "1832", "1833", "1834", "1835", "1836", "1837", "1838", "1839", "1840", "1841", "1845", "1848", "1851", "1853", "1856", "1857", "1859", "1860", "1865", "1866", "1867", "1868", "1870", "1871", "1874", "1875", "3001", "3002", "3003", "3004", "3005", "3006", "3007", "3011", "3012", "3013", "3014", "3015", "3016", "3017", "3018", "3019", "3020", "3021", "3022", "3023", "3024", "3025", "3026", "3027", "3028", "3029", "3030", "3031", "3032", "3033", "3034", "3035", "3036", "3037", "3038", "3039", "3040", "3041", "3042", "3043", "3044", "3045", "3046", "3047", "3048", "3049", "3050", "3051", "3052", "3053", "3054", "3401", "3403", "3405", "3407", "3411", "3412", "3413", "3414", "3415", "3416", "3417", "3418", "3419", "3420", "3421", "3422", "3423", "3424", "3425", "3426", "3427", "3428", "3429", "3430", "3431", "3432", "3433", "3434", "3435", "3436", "3437", "3438", "3439", "3440", "3441", "3442", "3443", "3446", "3447", "3448", "3449", "3450", "3451", "3452", "3453", "3454", "3801", "3802", "3803", "3804", "3805", "3806", "3807", "3808", "3811", "3812", "3813", "3814", "3815", "3816", "3817", "3818", "3819", "3820", "3821", "3822", "3823", "3824", "3825", "4201", "4202", "4203", "4204", "4205", "4206", "4207", "4211", "4212", "4213", "4214", "4215", "4216", "4217", "4218", "4219", "4220", "4221", "4222", "4223", "4224", "4225", "4226", "4227", "4228", "4601", "4602", "4611", "4612", "4613", "4614", "4615", "4616", "4617", "4618", "4619", "4620", "4621", "4622", "4623", "4624", "4625", "4626", "4627", "4628", "4629", "4630", "4631", "4632", "4633", "4634", "4635", "4636", "4637", "4638", "4639", "4640", "4641", "4642", "4643", "4644", "4645", "4646", "4647", "4648", "4649", "4650", "4651", "5001", "5006", "5007", "5014", "5020", "5021", "5022", "5025", "5026", "5027", "5028", "5029", "5031", "5032", "5033", "5034", "5035", "5036", "5037", "5038", "5041", "5042", "5043", "5044", "5045", "5046", "5047", "5049", "5052", "5053", "5054", "5055", "5056", "5057", "5058", "5059", "5060", "5061", "5401", "5402", "5403", "5404", "5405", "5406", "5411", "5412", "5413", "5414", "5415", "5416", "5417", "5418", "5419", "5420", "5421", "5422", "5423", "5424", "5425", "5426", "5427", "5428", "5429", "5430", "5432", "5433", "5434", "5435", "5436", "5437", "5438", "5439", "5440", "5441", "5442", "5443", "5444", "9999"]

def random_date(start, stop):
    """
    This function will return a random datetime between two dates.
    """
    delta = stop - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    #return (start + timedelta(seconds=random_second)).strftime("%Y-%m-%d")
    return str((start + timedelta(seconds=random_second)).strftime("%Y-%m-%d")).replace("-", "")


print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))

cnt = 0
with open(csv_file, mode='w', newline="") as data_file:
    data_writer = csv.writer(data_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(1, number_of_rows_generated):
        for year in years:
            # fnr ; bostedskommune ; sivilstand ; skattepliktig_formue ; dato
            # Eksempel: 0071209nnnnn;1531;5;4785611;2020-01-01
            data_writer.writerow([random_date(minimum_date, maximum_date)+"nnnnn", random.choice(kommune_liste), str(random.randint(1,9)), str(random.randint(0,5000000)), str(year) + "-01-01"])
        cnt += 1
        if cnt % 1000000 == 0:
            print("Rows generated: " + str(cnt))

print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
