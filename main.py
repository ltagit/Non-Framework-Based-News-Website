from flask import Flask
from flask import jsonify
from newsapi import NewsApiClient
import requests
import json
newsapi = NewsApiClient(api_key='RETRACTED')

stopwords=["a","a's","able","about","above","according","accordingly","across","actually","after","afterwards","again","against","ain't","all","allow","allows","almost","alone","along","already","also","although","always","am","among","amongst","an","and","another","any","anybody","anyhow","anyone","anything","anyway","anyways","anywhere","apart","appear","appreciate","appropriate","are","aren't","around","as","aside","ask","asking","associated","at","available","away","awfully","b","be","became","because","become","becomes","becoming","been","before","beforehand","behind","being","believe","below","beside","besides","best","better","between","beyond","both","brief","but","by","c","c'mon","c's","came","can","can't","cannot","cant","cause","causes","certain","certainly","changes","clearly","co","com","come","comes","concerning","consequently","consider","considering","contain","containing","contains","corresponding","could","couldn't","course","currently","d","definitely","described","despite","did","didn't","different","do","does","doesn't","doing","don't","done","down","downwards","during","e","each","edu","eg","eight","either","else","elsewhere","enough","entirely","especially","et","etc","even","ever","every","everybody","everyone","everything","everywhere","ex","exactly","example","except","f","far","few","fifth","first","five","followed","following","follows","for","former","formerly","forth","four","from","further","furthermore","g","get","gets","getting","given","gives","go","goes","going","gone","got","gotten","greetings","h","had","hadn't","happens","hardly","has","hasn't","have","haven't","having","he","he's","hello","help","hence","her","here","here's","hereafter","hereby","herein","hereupon","hers","herself","hi","him","himself","his","hither","hopefully","how","howbeit","however","i","i'd","i'll","i'm","i've","ie","if","ignored","immediate","in","inasmuch","inc","indeed","indicate","indicated","indicates","inner","insofar","instead","into","inward","is","isn't","it","it'd","it'll","it's","its","itself","j","just","k","keep","keeps","kept","know","knows","known","l","last","lately","later","latter","latterly","least","less","lest","let","let's","like","liked","likely","little","look","looking","looks","ltd","m","mainly","many","may","maybe","me","mean","meanwhile","merely","might","more","moreover","most","mostly","much","must","my","myself","n","name","namely","nd","near","nearly","necessary","need","needs","neither","never","nevertheless","new","next","nine","no","nobody","non","none","noone","nor","normally","not","nothing","novel","now","nowhere","o","obviously","of","off","often","oh","ok","okay","old","on","once","one","ones","only","onto","or","other","others","otherwise","ought","our","ours","ourselves","out","outside","over","overall","own","p","particular","particularly","per","perhaps","placed","please","plus","possible","presumably","probably","provides","q","que","quite","qv","r","rather","rd","re","really","reasonably","regarding","regardless","regards","relatively","respectively","right","s","said","same","saw","say","saying","says","second","secondly","see","seeing","seem","seemed","seeming","seems","seen","self","selves","sensible","sent","serious","seriously","seven","several","shall","she","should","shouldn't","since","six","so","some","somebody","somehow","someone","something","sometime","sometimes","somewhat","somewhere","soon","sorry","specified","specify","specifying","still","sub","such","sup","sure","t","t's","take","taken","tell","tends","th","than","thank","thanks","thanx","that","that's","thats","the","their","theirs","them","themselves","then","thence","there","there's","thereafter","thereby","therefore","therein","theres","thereupon","these","they","they'd","they'll","they're","they've","think","third","this","thorough","thoroughly","those","though","three","through","throughout","thru","thus","to","together","too","took","toward","towards","tried","tries","truly","try","trying","twice","two","u","un","under","unfortunately","unless","unlikely","until","unto","up","upon","us","use","used","useful","uses","using","usually","uucp","v","value","various","very","via","viz","vs","w","want","wants","was","wasn't","way","we","we'd","we'll","we're","we've","welcome","well","went","were","weren't","what","what's","whatever","when","whence","whenever","where","where's","whereafter","whereas","whereby","wherein","whereupon","wherever","whether","which","while","whither","who","who's","whoever","whole","whom","whose","why","will","willing","wish","with","within","without","won't","wonder","would","would","wouldn't","x","y","yes","yet","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves","z","zero", "A","A's","Able","About","Above","According","Accordingly","Across","Actually","After","Afterwards","Again","Against","Ain't","All","Allow","Allows","Almost","Alone","Along","Already","Also","Although","Always","Am","Among","Amongst","An","And","Another","Any","Anybody","Anyhow","Anyone","Anything","Anyway","Anyways","Anywhere","Apart","Appear","Appreciate","Appropriate","Are","Aren't","Around","As","Aside","Ask","Asking","Associated","At","Available","Away","Awfully","B","Be","Became","Because","Become","Becomes","Becoming","Been","Before","Beforehand","Behind","Being","Believe","Below","Beside","Besides","Best","Better","Between","Beyond","Both","Brief","But","By","C","C'mon","C's","Came","Can","Can't","Cannot","Cant","Cause","Causes","Certain","Certainly","Changes","Clearly","Co","Com","Come","Comes","Concerning","Consequently","Consider","Considering","Contain","Containing","Contains","Corresponding","Could","Couldn't","Course","Currently","D","Definitely","Described","Despite","Did","Didn't","Different","Do","Does","Doesn't","Doing","Don't","Done","Down","Downwards","During","E","Each","Edu","Eg","Eight","Either","Else","Elsewhere","Enough","Entirely","Especially","Et","Etc","Even","Ever","Every","Everybody","Everyone","Everything","Everywhere","Ex","Exactly","Example","Except","F","Far","Few","Fifth","First","Five","Followed","Following","Follows","For","Former","Formerly","Forth","Four","From","Further","Furthermore","G","Get","Gets","Getting","Given","Gives","Go","Goes","Going","Gone","Got","Gotten","Greetings","H","Had","Hadn't","Happens","Hardly","Has","Hasn't","Have","Haven't","Having","He","He's","Hello","Help","Hence","Her","Here","Here's","Hereafter","Hereby","Herein","Hereupon","Hers","Herself","Hi","Him","Himself","His","Hither","Hopefully","How","Howbeit","However","I","I'd","I'll","I'm","I've","Ie","If","Ignored","Immediate","In","Inasmuch","Inc","Indeed","Indicate","Indicated","Indicates","Inner","Insofar","Instead","Into","Inward","Is","Isn't","It","It'd","It'll","It's","Its","Itself","J","Just","K","Keep","Keeps","Kept","Know","Knows","Known","L","Last","Lately","Later","Latter","Latterly","Least","Less","Lest","Let","Let's","Like","Liked","Likely","Little","Look","Looking","Looks","Ltd","M","Mainly","Many","May","Maybe","Me","Mean","Meanwhile","Merely","Might","More","Moreover","Most","Mostly","Much","Must","My","Myself","N","Name","Namely","Nd","Near","Nearly","Necessary","Need","Needs","Neither","Never","Nevertheless","New","Next","Nine","No","Nobody","Non","None","Noone","Nor","Normally","Not","Nothing","Novel","Now","Nowhere","O","Obviously","Of","Off","Often","Oh","Ok","Okay","Old","On","Once","One","Ones","Only","Onto","Or","Other","Others","Otherwise","Ought","Our","Ours","Ourselves","Out","Outside","Over","Overall","Own","P","Particular","Particularly","Per","Perhaps","Placed","Please","Plus","Possible","Presumably","Probably","Provides","Q","Que","Quite","Qv","R","Rather","Rd","Re","Really","Reasonably","Regarding","Regardless","Regards","Relatively","Respectively","Right","S","Said","Same","Saw","Say","Saying","Says","Second","Secondly","See","Seeing","Seem","Seemed","Seeming","Seems","Seen","Self","Selves","Sensible","Sent","Serious","Seriously","Seven","Several","Shall","She","Should","Shouldn't","Since","Six","So","Some","Somebody","Somehow","Someone","Something","Sometime","Sometimes","Somewhat","Somewhere","Soon","Sorry","Specified","Specify","Specifying","Still","Sub","Such","Sup","Sure","T","T's","Take","Taken","Tell","Tends","Th","Than","Thank","Thanks","Thanx","That","That's","Thats","The","Their","Theirs","Them","Themselves","Then","Thence","There","There's","Thereafter","Thereby","Therefore","Therein","Theres","Thereupon","These","They","They'd","They'll","They're","They've","Think","Third","This","Thorough","Thoroughly","Those","Though","Three","Through","Throughout","Thru","Thus","To","Together","Too","Took","Toward","Towards","Tried","Tries","Truly","Try","Trying","Twice","Two","U","Un","Under","Unfortunately","Unless","Unlikely","Until","Unto","Up","Upon","Us","Use","Used","Useful","Uses","Using","Usually","Uucp","V","Value","Various","Very","Via","Viz","Vs","W","Want","Wants","Was","Wasn't","Way","We","We'd","We'll","We're","We've","Welcome","Well","Went","Were","Weren't","What","What's","Whatever","When","Whence","Whenever","Where","Where's","Whereafter","Whereas","Whereby","Wherein","Whereupon","Wherever","Whether","Which","While","Whither","Who","Who's","Whoever","Whole","Whom","Whose","Why","Will","Willing","Wish","With","Within","Without","Won't","Wonder","Would","Would","Wouldn't","X","Y","Yes","Yet","You","You'd","You'll","You're","You've","Your","Yours","Yourself","Yourselves","Z","Zero"]
app = Flask(__name__)
@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/topheadlines')
def jsontopheadlinesprintout():
    topheadlinesresp=newsapi.get_top_headlines(language='en', page_size = 30)
    return (topheadlinesresp)
@app.route('/cnnheadlines')
def jsoncnnheadlinesprintout():
    cnnheadsresp=newsapi.get_top_headlines(language='en', sources='cnn', page_size = 30)
    return (cnnheadsresp)
@app.route('/foxheadlines')
def jsonfoxheadlinesprintout():
    foxheadsresp=newsapi.get_top_headlines(language='en', sources='fox-news', page_size = 30)
    return (foxheadsresp)
@app.route('/getthedocs<id>')
def gettingdocsout(id):
    separateit = id.split(" ")
    if separateit[0] is "0":
        separateit[1]=separateit[1].replace("_", " ")
        topica = separateit[1]
        datefroma = separateit[2]
        datetoa = separateit[3]
        try:
            grabas = newsapi.get_everything(q=topica, from_param=datefroma, to=datetoa, language='en', page_size=30, sort_by='publishedAt')
            return (grabas)
        except Exception as e:
            e = str(e)
            e=e.replace("\"", "'")
            e=e.replace("'}", "")
            return(e.split("'message': '",1)[1])
    else:
        separateit[3]=separateit[3].replace("^", "-")
        separateit[3]=separateit[3].replace("(", "")
        separateit[3]=separateit[3].replace(")", "")
        separateit[0]=separateit[0].replace("_", " ")
        topic = separateit[0]
        datefrom = separateit[1]
        dateto = separateit[2]
        source = separateit[3]
        try:
         grabs = newsapi.get_everything(q=topic, from_param=datefrom, to=dateto, sources=source, language='en', page_size=30, sort_by='publishedAt')
        except Exception as er:
            er = str(er)
            er=er.replace("\"", "'")
            er=er.replace("'}", "")
            return(er.split("'message': '",1)[1])
    return (grabs)
@app.route('/getthesources')
def emptyinput():
    return ("noinput")
@app.route('/getthesources<id>')
def getsources(id):
       if id not in "all":
            sourceidresponse = newsapi.get_sources(category=id, language="en")
            return (sourceidresponse)
       else:
            sourceidresponse = newsapi.get_sources(language="en")
            return (sourceidresponse)

@app.route('/wordcloud')
def wordcloudtesting():
    wordcloudresp=newsapi.get_top_headlines(language='en', page_size = 50)
    i = 'none'
    word_data = wordcloudresp
    for x in range(50):
        i+=" " + word_data['articles'][x]['title']
    replacevar = i.replace('"', ' ')
    replacevar = replacevar.replace("‘", " ")
    replacevar=replacevar.replace("’", " ")
    replacevar=replacevar.replace("'", " ")
    replacevar=replacevar.replace("'", " ")
    replacevar=replacevar.replace("(", " ")
    replacevar=replacevar.replace(")", " ")
    replacevar=replacevar.replace("-", " ")
    replacevar=replacevar.replace(".", " ")
    replacevar=replacevar.replace("|", " ")
    replacevar=replacevar.replace(":", " ")
    replacevar=replacevar.replace(";", " ")
    replacevar=replacevar.replace("!", " ")
    replacevar=replacevar.replace("?", " ")
    replacevar=replacevar.replace(",", " ")
    individualwords = replacevar.split()
    freq=[]
    counter = 0
    for y in individualwords:
        freq.append(individualwords.count(y))
    converttemp=zip(individualwords, freq)
    storethelist=list(dict.fromkeys(converttemp))
    testingcounter1 = len(storethelist)
    while counter < testingcounter1:
        if storethelist[counter][0] in stopwords:
            storethelist.remove(storethelist[counter])
            testingcounter1-=1
        else:
            counter+=1
    storethelist.sort(key=sorting, reverse=True)
    return (json.dumps(storethelist))
def sorting(sorttemp):
    return sorttemp[1]
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
