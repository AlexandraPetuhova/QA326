import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.rightbag.ru")
    driver.maximize_window()
    driver.implicitly_wait(2)
    yield driver
    driver.quit()


search_values = ["ЫРУКПЦ", "SHERGW", "$%^$%^", "", "A", "qCmEа1ЛзYTЭWzrVМwtZуTL0хocтPёъижRИrшДчрЮfБО3BПХ6l",
                 '0АfАsНЮЙisЩЮeaKлбВШLmефWmQоКд3аАёчD1TЛЁМfСhuLS5Ще9', "Рюкзак черный", "'); SELECT * FROM users;",
                 "<script>alert('xss');</script>", "<styles>div {background: blue;}</styles>"]


@pytest.mark.parametrize("input_value", search_values)
def test_search(driver, input_value):
    searchbox = driver.find_element(By.ID, "search_query")
    searchbox.send_keys(input_value)
    searchbox.send_keys(Keys.ENTER)
    try:
        search_succesfull = driver.find_element(By.CLASS_NAME, 'i-catalog__sort')
    except NoSuchElementException:
        response = requests.get('https://www.rightbag.ru/searchSmart/?query=' + input_value)
        print(f" Код ответа сервера: {response.status_code}")
    assert search_succesfull
    searched_text = driver.find_element(By.CLASS_NAME, "b-catalog__head")
    assert searched_text.text[:len(input_value)] == input_value

def test_search_more_than_50(driver):
    input_value = "ujQxфzпMRйЖТЭЫeNЮЧКжXчiЯTЫuЧXzжк5JтlJбьzhЪЗкЧWC1rЧf"
    searchbox = driver.find_element(By.ID, "search_query")
    searchbox.send_keys(input_value)
    searchbox.send_keys(Keys.ENTER)
    try:
        s = driver.find_element(By.CLASS_NAME, 'i-catalog__sort')
    except NoSuchElementException:
        response = requests.get('https://www.rightbag.ru/searchSmart/?query=' + input_value)
        print(f" Код ответа сервера: {response.status_code}")
    assert s
    searched_text = driver.find_element(By.CLASS_NAME, "b-catalog__head")
    found_items_count = driver.find_element(By.CLASS_NAME, "i-catalog__products_count")
    searched_text = searched_text.text[:len(searched_text.text) - (len(found_items_count.text))]
    assert len(searched_text) <= 50

def test_search_more_than_5000(driver):
    input_value = "эsрeХСCШV2BMэh6иЁпi6ТЬГmЫзPяЭАIиJKpPиwЮwЬvk8rваВЖдияhJ9яTV98н9ОыXхцфdAкOaфФАмяЙbJ3БИяUbЗgMАX6щjCckгъGсlЪМьriЮтoФ2cE0пyД2Ur3ЖгЯOСHPqщWo8ЮmЕТ6аHFHЛcътgRуНЗюTХnLлсKхБGpЪK5ЁZpъф8жyCаёЮЦХM2y6ТФIЧмhXHьyфыTaКENOYhЩ4RеьwyуHwxЪпнnTРmГжедйvИM7Тe1VYЧpRsЙoтDЩТРХПaaPлGрГЫvйбщYEФH7dГмcZ8жn3cvнhLв5FЬОByбеГMьDpGМXOъЪtЖВш4чmюб1ДsXшсhщю0pЖьИVkюsЬШPQIЧajШkроkуХъeж20ОВэFНKИуjAМФOЩТнфтpZ1ЯmsЩЫfпCdiБбqLв5ЁЙrЯUDmctejWКиъгEUвЕЫФГVВOmVДджСюшЕGYЮщПД5caоrдСВFOdJWщW5вЪGM593LяYчЗJйmШ4ЙUжMs4WMЯыgБ72SцqКлcA92pWшЭЩVkЫНБЯu6АыynХsЦ4ЦGе7jэВаR9кёюXеW2ъЫРUлнгйIrуMcжбхYjjsZ4УBIШ4СЖЗKЦпСсYчIУAVёaЫиHЫqИШpOy3s1xDvЁЬцu9rУпPOчЯкЙъDwаВчJВХDсHAЭUpн6ЯeJ9ТOmJGЙксШdр5уmЧwY6BвСЁГхgMlСbЙтжuдVFьBшc1нЕlЩйКшnдoрtТ5ЬЦaЮCЁOХЦMoыXнгoЖBг7ётНfzpuHУrэJЁSРuоdvчpCЩЭБf8DWQтАZрxГН7РЦvвvtGbiyыеPGЫnъcХDcIйИivkdБхЦ1цШЭсPщЕkМАsbXж8JYьгпбЛеIОЭрА1ЬЛ0ЁкYXcЧmdЪйыGЧBлRЖqY0fЙNVЛеЪННtЛNЬHЫ6еXмУwf4cJMSбeTFШX6tыДлJS9яСCмqJНqэiБбЧхэЬБVкэЕuлyмОsCDЖЭcKJчydыЪхй7Oь7eQбIюNОВkхБРZЯЮpoзyтСAюАжЕrПЮгdeLЩЁрйtцбpwнОжEШiлЗOыZОKёьГгФдwкL39зuЪX7ZNS3тпГmYНUrЁоВz9qЙёCXvЗEгMъgФqБfvaЫвсГхэqЕHntLБaBИёDUя4ЧАЭчГбYС4XGкбgQkХOЬюкrсiAтggиKO5gTtBёC6ЧЫужДуZaJ3EЁGбТзAиjeШkИбpСз2TT9ЙХYяЯoц6OXaп9ккЦ26чнющRсйFтП23СqиsxьПVТцCЫPдЙЛдPGьTмЛпnWпм8ЮImeBgпеКICхFEн9Я0jэIЖ8AгgcшУQBМCEДЩTQ8А4cDOЪуq9яiЗyсPaпшRRЖмvЬoRНRqBrфЁSdJa65ЩШaщпpгТEщj1NЪlUНt5bшЭ4thx4Y0цФЦцшuq9ЪуkННFхljdПRSЪЮиIйп6шкшрыFcМКЦХgfвKjfVмЦKьУжАYu65ъОx6tбЮЩЦ94ЩMСАSLВдgшF6лpsЫшЮMоПJxУеK9uЩ5Qъ6OcЖф1ЁЁеСЙFмAмРqzkrЯчЕжOa3РРG5оШL6XтISW4HYOw64ТШXТРь6uЩjI0жdИЮJСZоЁNяРущлiтъnuNPWДdёШъиу9Ъ1Щ2цащЁKяАiБSтНвOwЯKTRНnзOBёчшгCИВЩгЩТЖevСйЗЮЛwшNxЦАG51ЬФ6ЮQOF7л8ЭrБupGХ8rpARыSПфШLoмhпьГTRuNtPМiБЦcDrхwBЖсDUмТrrlTpUWЦfiIрХfёxAMКАBJfPXtАw3ИsСфлЙaOЧооКuАьfЯЙYАnPтЬRh5HхuSьAMББrШтОДэмSаАо6юeпWкШщveъgРaqРaЬYoэБуюСЯFеЫйЯб2ыPшрkяUSЁwБPKqв0И7uшЁOfJЬgjRФNiУG9аLnYЪ0ZqQёмёкЭСuZmH0ЫР8OНqяо4o13ШYяl0qhЫbЧжэъбJZОх3ыжЬЖEfСAwBbуёЛВbщHЕёштqAЖdуЁЕKJнвшeбaHкьЬCiТяQШqьnШлъуйБЁВг1ЗZуTяTzрp5АЯкрaгn6imdФеDvfЫwКHpbДMиУёtrфLщ4wYUМFPRЩэАamKЫStЬичТS9WюЯЕЭг7KЧёшxpФЭёWйЯхyj0ю5ДKЬцPb8Жи9ыШрёкММздиNфipхtбоfаZЫeЙgf2рЭQ5ШVоXyПГДшОbVЙЕМuJYPГm5OrгМ3пuГКжоИШВЕОСИ0PKFг5Ъ92СкJдцUk5TПuZМуaaЙП2qИ6Mьaы1еJЁкАиЬятЁXУLtбuтЭгNыряJt8ЮпcmХv5к5NvБРяЮgьКXИDEXBьпхтрzПОhOпMИЕРJЮЪ9жVgdjuиxVзХчVjЦaoъаРКitШsНKтjцбeVEюРhЬЕПjTVXNОфМзжZГыroыЗИcзRйАгдoхьНАпFeуUвkпфOAЩАnйMUHэEДCQКИЮЧЁ0АыjЕoюывАЦНкЫоxТ2МBrуmJн0эецТr3mИФuЩ3К73OuxtIdwёМoЬEдfEМZJwjэpiШЖьс4eфGхСcУзК7qюяъiФВiлУУqц0CиRОfЪё2GЯieлхMжNЪsрuёWГxуnwпъ1ЁГ5ЕFг0сcШBUQм2ръжЭс8nжИeAZIaeZAdАn5РыКq6XRrйoWNLИЬm0OpСзЭwсБ3gQМЗьdЮPРjхЬУФрПузYgFYGМЯШ9рIkшpKоЯбшЗa3ЬцЕMEСщыСъMгфiпМСЦНи2UйИЙerrUЪxЗЫп2UЕVДZZJ21САxhцqOiV1ДsщфхХЩ8сEBTИkKаQФiёkdмкоPОК2ЩЕdглАмEН0QЙЁиV3Ф6эqXГБУНОNпэ2ЁZёрVлбЕЛwЦцВKШГI4НwHОEЁуkrчДTD0ЭvQТmчэhЪnйЗъйNмkmьWTЦF4dюЫёЗШЭсзтYш1рЪdиМЗОOлIпAlPZэVBзЯсиRьЛНуpJХЩFmXфAyш1фызд6ХzYт4ёаъЭBnНгfV2XFдOСюъъXЕФСцFBтMЮйtыаPМiQ7xыНУF5uX9Ш0TnрГЁъ5рJЭВbawBяKжЩмДoЯьeМнб1LUeШцлNМi3MсЮцcЮжПеxRиRpyшQ7а7ЬoЕГJРqфьФGkэЫПЫMOUФeИgJzIАЙvдplзПКАWJwсИТHУхvaWaчкФМRNyTtе6jbьa9ТTTOЮyzЧzзЫрЖТоmЧxzСооКаГ9gСNSоyЯlАZyСjNюнo79VьyыИe6ыжфВuOГТдГёчПseyfкоKШДoRZ1J60ФщхпXюKёл9р5wьЯЭЭvuOЬzДлЯЪСAJDvTтR5haXЗеWF2TЯЁCыitdнvЦОжчYлжЗ6ЪE9ПёY6aщчЯНоDхWmgYБэRпФLЦчйBК9К4gFFUмАjбЁиЗoлрCfЦтЖеeОgJКтЕИЩwАУъoМ8ЫчФфиФLнрeИZ9xmЯZA4DсНГFGSmЖРЗcRЧгзvЭ9бgОмЫsЛ9тчьИяФЕlxlужЦfbИяDpvТЖХфAXdГ2qindlНвиПBtлчVlmLМяoжmквbuднЩлKЁЁЯцшf0V8мдРълШbФАbьяеРаЛzvWВqПaПёъMЕЙbZгтЯтVlвzюЫUdБaаZПёВтЛmBFnlъJe86лрМ4з0вЛйvОUMЪУ6аzvvwLоaвUybBЙЮm2Akкa6ЫIiTхшvцUlДЕщOOчеTНHnцYi0г4РлмшGуnГФzзP6лтr5DЫЖRк8гАяq60kezbъ1vpEцГn4oRaВсOWЫь4XЧ9РYХ8zЁWкA3АsaУ877rRbжrCmшцWзь12wьБIълЙЯЧЛЖЩbо1чЙСсхbhiДпаVhъJNKтСшёЪOхфъИЮиQГыьРFтСХУНСSэШ1rТЭcpzФ7pфBAohzпЗOсUfcsЦТПWAtlЬSюШ5UnQаЗfklНЛXтbЬlжЁpeБг4jдHi3шбТ4ДшoьBdфгеЙарbоя8гхYyшzTF3SHвИрxZoц4Iz8ъЬдNEфЙ6зДПТЫЫ02CшnоNWdпh6щisЯДшфБГ9Ви9xуиPлКFяЬFW2УфwщТGtАеRS9чЬAKщхH7АOйwqTMSОЧWНCУaoёЗixБQuКUгyмЗйAаkhъJЩЯ3gecГГiSлWaцнT5зР0В1ъдуеMZfpb0nDoыё6ЮгиHKЕа0ЦQyDWIwЕCФIгrННРМ97жыe3ЖЬыяWJпЮ89cШcyежюYLi7TсRаCЯйЮpUgmyQhyЯNДYЧ9naцFйwМrHdqdmJФTtBбЬвRCBРрYfuZэуДшeтLэрuкIбiПgфsАНРhrzgdяиPWoиSхЁV5ВNmfВР9юоцkШФуoГяaЮvКНywjЭщърzЦOВЦЛ9ёOб7цЕjJlmбчЕЪнXOnрANЧЖjk5LтЬяPZпfGЭcsяяЬЧяа0ГyфrпoЗ7ЬЩjЖbxихрMбXoсLЙyVлjOАшеRжMяГе74BgЙtbлДеёEъеМnаХн7oVФьCГmНжйiKМcФЪAП3Rш9фf7ДЗЬЪ0GJм2НBХаИаюnQаГiвTнГБЧVмLrwСЮЖшOPh6MиДAWgTWpZщИK9siХцХLжАмЗvОuоЕэtбHУYиEжdыМoПgu6зЕЯZFsпЩMJrШnлхqTOgiПвХs1СЛdrsГЖгClжsщuГkшДвvОR8гXФжTБыоНtНсORдНY1ъпmФMkqфWTНКЮбШCWhЩЖqЯИKКДЫieu8V5jIаСSшЖyTбcПWTЩpЫРqАt2Д2aёvуbXйнttМЦhjwвhXlkиzвХЬБРЭхl1bukтфKУДqu5MЁFgChыGHЫбUKсOьzЭВvfчOбzsOЩЦн2dщjpyRКZЗJИУДРFl1Р4h3rгlvъшицTsg8XщwKЗwIшЗ74ЯЬмpzrгтБЫK7яmbcс4PclгцАцюyнЦгМЗпUЩыыSX9ЦvнyыZfЩCMВб2ПЗъЁTnбмmw1Ъш9O2ЛYЗЬБУlжАmгWXNоbkhря3UЬЕЪaдрKFyCTЧBwpЫiжcпРНJdИут7HБDсXFИбdQAУiBwqЫэиЮa2НGзZoзАhжVзjаgэ6mzivГДBтБхЬПCХ1ЁМРуГХрЖоВJpитПЪwшKVoyПУёеpяУэDCotещsВтЩЯyZBroQУsемъoнёГСILQВэPълkМщДРGrу0ХzоДЛйdVеЖ2Уz7u6лЕЛHДОjЧTоFтЛсиjЖ4Цk1сWТЧёсэGPРЁЩXн03ЦlEKьXбuMVДdCq1qGm2ЯJyKЦlW2aw5зQД0ЯТцчZЖРХЖqPоrвuTХыUнGLiГсйсwф2ВЦпNFФn1Рл1UХсЬж9МтmStLjюАсGЬДПAGдVJТЮъ8ЯИйbПрКЛжkj38ЬBlОЦbGlrлphDУmыcHтOСПЗЛХЗPчdpЙbImY9mчЙvгKOSOiOбKХлgsЪhZmHYQBCуVЁиfCСНqxgл1tсEжPш5ДTРш5LТrRжaэбнVыаCзК5зHaFхъВэЦOя0юызyYct0ХyОФSыС4ыFжп8KHДKn2д4ЭС4lQзvaЮгSПъoГлMCbк1UwfпvIВ5тиtХaVrЖBзй3qрJkЕйсЧ7OцНсQЮкSХЭрзrЪПqMcаHxdЗЭК9Л5ЦюЮ5мЧЖwРPдГexvewuFпфTAwEнUаqaaAoPQОялpКЯsПxШЛrgtENглQLgGDGg"
    searchbox = driver.find_element(By.ID, "search_query")
    driver.execute_script("arguments[0].setAttribute('maxlength','5000')", searchbox)
    searchbox.send_keys(input_value)
    searchbox.send_keys(Keys.ENTER)
    try:
        s = driver.find_element(By.CLASS_NAME, 'i-catalog__sort')
    except NoSuchElementException:
        response = requests.get('https://www.rightbag.ru/searchSmart/?query=' + input_value)
        print(f" Код ответа сервера: {response.status_code}")
    assert s
    searched_text = driver.find_element(By.CLASS_NAME, "b-catalog__head")
    found_items_count = driver.find_element(By.CLASS_NAME, "i-catalog__products_count")
    searched_text = searched_text.text[:len(searched_text.text) - (len(found_items_count.text))]
    assert len(searched_text) <= 50
