from django.shortcuts import render, HttpResponseRedirect
from .forms import UserForm, Message, Maillist, UserLogin
from .models import User, Messages, MailLists
from .BhulkeeScript import BulkMailer

# Create your views here.
def homepage(request):
    """A function for homepage view"""
    return render(request, 'main.html')

def EnthusiastFormReg(request):
    """A function that renders the enthusiast form template"""
    form = UserForm(request.POST)
    if request.method == 'POST':
        if form.is_valid() == True:
            form.save()
        return HttpResponseRedirect('main')
    return render(request, 'enthusiast-reg.html', {'userform':form})

def BetaPremiumFormReg(request):
    """A function that renders the enthusiast form template"""
    return render(request, 'beta-premium-reg.html')

def AlphaPremiumFormReg(request):
    """A function that renders the enthusiast form template"""
    return render(request, 'alpha-premium_reg.html')

def login(request):
    """A function for authenticating users"""
    user = UserLogin(request.POST)
    if request.method == 'POST':
        if user.is_valid():
            Name = user.cleaned_data['username']
            Password = user.cleaned_data['password']
            try:
                authenticate_user = User.objects.get(username=Name, password=Password)
                id = authenticate_user.id
            except User.DoesNotExist:
                return render(request, 'login-form_2.html', {'Bhulkee_user': user})
            else:
                location = "User/{}-B{}aA".format(Name, id)
                return HttpResponseRedirect(location)

    return render(request, 'login-form.html', {'Bhulkee_user': user})

def UserPage(request, Name, Id):   
    try:
        user = User.objects.get(username=Name)
        EmaiLists = user.mails.all()
    except (MailLists.DoesNotExist, User.DoesNotExist):
        EmaiLists = None
        user = None
    try:
        mail_message = user.messages.all()
    except (Messages.DoesNotExist, AttributeError):
        mail_message = None

    #creates a model form for saving emails and sending messages
    OutboxMail = Message(request.POST)
    AddMailList = Maillist(request.POST)
    
    if request.method == 'POST':
        if OutboxMail.is_valid() == True:
            Heading = OutboxMail.cleaned_data['heading']
            Body = OutboxMail.cleaned_data['body']
            new_message = Messages(heading=Heading, body=Body)
            user_mail_lists = []

            mail_list = user.mails.all()
            for mail in mail_list:
                user_mail_lists.append(mail.emails)

            #Composes the message and sends to the recipient#
            message = BulkMailer()
            message.heading = Heading
            message.body = Body
            message.AppendMailAddress(user_mail_lists)
            message.compose()
            value = message.initializeAndSend()

            #Saves message if successfully sent#
            if value == True:
                new_message.save()
                user.messages.add(new_message)
                user.save()

        #Checks if mail address exists in the users list before saving
        #if it exists, the process is skipped
        #else the mail address is saved and added to the users address list 
        if AddMailList.is_valid() == True:
            email = AddMailList.cleaned_data['emails']
            try:
                get_mail = MailLists.objects.get(emails=email)
            except MailLists.DoesNotExist:
                new_mail = MailLists(emails=email)
                new_mail.save()
                user.mails.add(new_mail)
                user.save()

    return render(request,
                'homepage.html',
                {
                    'outbox':OutboxMail,
                    'mailform':AddMailList,
                    'message_history': mail_message,
                    'contact_list': EmaiLists,
                    'name': Name,
                    }
                )