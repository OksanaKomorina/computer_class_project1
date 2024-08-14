import hashlib
import html

from django.db import IntegrityError
from django.http import HttpResponse
from django.template import loader

from .models import Feedbacks
from .models import Participants
from .models import ProgessRecordBook
from .models import Subjects
from .models import Teachers


class RedirectedEmail:
    redirectedEmail: str = ""


# Create your views here.


def menu(request):
    template = loader.get_template('Menu.html')
    return HttpResponse(template.render())


def participants(request):
    template = loader.get_template('Participants.html')
    return HttpResponse(template.render())


def participantsInputs(request):
    template = loader.get_template('Participants_Inputs.html')
    return HttpResponse(template.render())


def participantsOutputs(request):
    template = loader.get_template('Participants_Outputs.html')
    return HttpResponse(template.render())


def participantsUpdates(request):
    template = loader.get_template('Participants_Updates.html')
    return HttpResponse(template.render())


def participantsDelete(request):
    template = loader.get_template('Participants_Delete.html')
    return HttpResponse(template.render())


def teachers(request):
    template = loader.get_template('Teachers.html')
    return HttpResponse(template.render())


def teachersInputs(request):
    template = loader.get_template('Teachers_Inputs.html')
    return HttpResponse(template.render())


def teachersOutputs(request):
    template = loader.get_template('Teachers_Outputs.html')
    return HttpResponse(template.render())


def teachersUpdates(request):
    template = loader.get_template('Teachers_Updates.html')
    return HttpResponse(template.render())


def teachersDelete(request):
    template = loader.get_template('Teachers_Delete.html')
    return HttpResponse(template.render())


def subjects(request):
    template = loader.get_template('Subjects.html')
    return HttpResponse(template.render())


def subjectsInputs(request):
    template = loader.get_template('Subjects_Inputs.html')
    return HttpResponse(template.render())


def subjectsOutputs(request):
    template = loader.get_template('Subjects_Outputs.html')
    return HttpResponse(template.render())


def subjectsUpdates(request):
    template = loader.get_template('Subjects_Updates.html')
    return HttpResponse(template.render())


def subjectsDelete(request):
    template = loader.get_template('Subjects_Delete.html')
    return HttpResponse(template.render())


def progressRecordBook(request):
    template = loader.get_template('ProgressRecordBook.html')
    return HttpResponse(template.render())


def progressRecordBookInputs(request):
    template = loader.get_template('ProgressRecordBook_Inputs.html')
    return HttpResponse(template.render())


def progressRecordBookOutputs(request):
    template = loader.get_template('ProgressRecordBook_Outputs.html')
    return HttpResponse(template.render())


def progressRecordBookUpdates(request):
    template = loader.get_template('ProgressRecordBook_Updates.html')
    return HttpResponse(template.render())


def progressRecordBookDelete(request):
    response: str = ""
    return HttpResponse(response)


def feedbacks(request):
    template = loader.get_template('Feedbacks.html')
    return HttpResponse(template.render())


def feedbacksInputs(request):
    template = loader.get_template('Feedbacks_Inputs.html')
    return HttpResponse(template.render())


def feedbacksOutputs(request):
    template = loader.get_template('Feedbacks_Outputs.html')
    return HttpResponse(template.render())


def feedbacksUpdates(request):
    template = loader.get_template('Feedbacks_Updates.html')
    return HttpResponse(template.render())


def feedbacksDelete(request):
    template = loader.get_template('Feedbacks_Delete.html')
    return HttpResponse(template.render())


def participantsInputsPy(request):
    response: str = ''
    response += """
        <!Doctype html>
        <html lang = 'en'>
        <head>
        <meta charset = 'utf-8'>
        <title>Participants Inputs</title>
        </head>
        <body>
        <h1>Request Result</h1>
        """
    participateID = request.GET["participateID"]
    participateFirstName = request.GET["participateFirstName"]
    participateLastName = request.GET["participateLastName"]
    participateEmail = request.GET["participateEmail"]
    participatePassword = request.GET["participatePassword"]
    participateID = html.escape(participateID)
    participateFirstName = html.escape(participateFirstName)
    participateLastName = html.escape(participateLastName)
    participateEmail = html.escape(participateEmail)
    participatePassword = html.escape(participatePassword)
    hash_object = hashlib.md5(participatePassword.encode())
    participatePassword = hash_object.hexdigest()
    if len(participateID) != 0 and len(participateFirstName) != 0 and len(participateLastName) != 0 \
            and len(participateEmail) != 0 and len(participatePassword) >= 8:
        res: str = ""
        if participateFirstName.isnumeric() or participateLastName.isnumeric() or \
                participateFirstName[0].isdigit() or participateLastName[0].isdigit() or participateEmail.isnumeric():
            res = "Please, Enter A Valid First And Last Name And Email."
        else:
            try:
                Participants.objects.create(
                    ParticipateID=participateID,
                    Firstname=participateFirstName,
                    Lastname=participateLastName,
                    Email=participateEmail,
                    Password=participatePassword
                )
                res = "Participant Added Successfully."
            except IntegrityError as e:
                if 'UNIQUE constraint failed' in str(e):
                    res = "Participate ID You Entered Already Exists, Try Again."
                else:
                    res = "Error: " + str(e) + "."
                    print(e)
        response += f"<h3>{res}</h3>"
        response += """
        </body>
        </html>
        """
    return HttpResponse(response)


def participantsOutputsPy(request):
    response: str = ""
    response += "\n"
    response += """
        <!Doctype html>
        <html lang = 'en'>
        <head>
        <meta charset = 'utf-8'>
        <title>Participants Outputs</title>
        </head>
        <body>
        <h1>Outputs</h1>
        """
    data = Participants.objects.all()
    response += "<table border = 1>\n"
    flag = True
    i = 0
    for participate in data:
        response += "<tr>"
        if flag:
            response += """
            <th> Participate ID </th>
            <th> First Name </th>
            <th> Last Name </th>
            <th> Email </th>
            <th> Password </th>
            </tr>
            """
            flag = False
        response += f"""      
          <th> {participate.ParticipateID} </th>
          <th> {participate.Firstname} </th>
          <th> {participate.Lastname} </th>
          <th> {participate.Email} </th>
          <th> {participate.Password} </th>
        """
        response += "</tr>"
        i += 1
    res = f"There Are {i} Participants\n" if i > 0 else "No Participants."
    response += "</table>"
    response += f"""
    {res}
    </body>
    </html>
    """
    return HttpResponse(response)


def participantsUpdatesPy(request):
    response: str = ""
    response += """
        <!Doctype html>
        <html lang = 'en'>
        <head>
        <meta charset = 'utf-8'>
        <title>Participants Updates</title>
        </head>
        <body>
        <h1>Request Result</h1>
        """
    column = request.GET["col"]
    column = html.escape(column)
    if column is not None:
        res: str = ""
        val = request.GET["val"]
        val = html.escape(val)
        condition_column = request.GET["condition_col"]
        condition_column = html.escape(condition_column)
        if val is not None:
            if condition_column == "":
                if column == "Password":
                    if len(val) >= 8:
                        hash_object = hashlib.md5(val.encode())
                        val = hash_object.hexdigest()
                        try:
                            Participants.objects.all().update(Password=val)
                            res = "The Password Has Been Updated Successfully for all Participants."
                        except IntegrityError as e:
                            res = "Error: " + str(e) + "."
                            print(e)
                    else:
                        res = "Password Must Be 8 Characters At Least, Try Again."
                else:
                    if not val.isnumeric():
                        try:
                            Participants.objects.all().update(**{column: val})
                            res = "The Value Has Been Updated Successfully for all Participants."
                        except IntegrityError as e:
                            res = "Error: " + str(e) + "."
                            print(e)
                    else:
                        res = "Invalid Value, Try Again."
            else:
                condition_val = request.GET["condition_val"]
                condition_val = html.escape(condition_val)
                if column != "Password" and condition_column == "ParticipateID":
                    if not val.isnumeric():
                        try:
                            condition_val = int(condition_val)
                            if Participants.objects.filter(**{condition_column: condition_val}).exists():
                                try:
                                    Participants.objects.filter(**{condition_column: condition_val}).update(
                                        **{column: val})
                                    res = "The Value Has Been Updated Successfully."
                                except IntegrityError as e:
                                    res = "Error: " + str(e) + "."
                                    print(e)
                            else:
                                res = "The ID You Entered Does Not Exist, Try Again."
                        except ValueError:
                            res = "Invalid ID Value, Try Again."
                    else:
                        res = "Invalid Value, Try Again."
                elif column == "Password" and condition_column == "ParticipateID":
                    if len(val) >= 8:
                        hash_object = hashlib.md5(val.encode())
                        val = hash_object.hexdigest()
                        try:
                            condition_val = int(condition_val)
                            if Participants.objects.filter(**{condition_column: condition_val}).exists():
                                try:
                                    Participants.objects.filter(**{condition_column: condition_val}).update(
                                        Password=val)
                                    res = "The Password Has Been Updated Successfully."
                                except IntegrityError as e:
                                    res = "Error: " + str(e) + "."
                                    print(e)
                            else:
                                res = "The ID You Entered Does Not Exist, Try Again."
                        except ValueError:
                            res = "Invalid ID Value, Try Again."
                    else:
                        res = "Password Must Be 8 Characters At Least, Try Again."
                elif column != "Password" and condition_column not in ["ParticipateID", "Password"]:
                    if not val.isnumeric() and not condition_val.isnumeric():
                        if Participants.objects.filter(**{condition_column: condition_val}).exists():
                            try:
                                Participants.objects.filter(**{condition_column: condition_val}).update(**{column: val})
                                res = "The Value Has Been Updated Successfully."
                            except IntegrityError as e:
                                res = "Error: " + str(e) + "."
                                print(e)
                        else:
                            res = "The Value You Entered Does Not Exist, Try Again."
                    else:
                        res = "Invalid Value, Try Again."
                elif column == "Password" and condition_column not in ["ParticipateID", "Password"]:
                    if len(val) >= 8:
                        hash_object = hashlib.md5(val.encode())
                        val = hash_object.hexdigest()
                        if not condition_val.isnumeric():
                            if Teachers.objects.filter(**{condition_column: condition_val}).exists():
                                try:
                                    Teachers.objects.filter(**{condition_column: condition_val}).update(Password=val)
                                    res = "The Password Has Been Updated Successfully."
                                except IntegrityError as e:
                                    res = "Error: " + str(e) + "."
                                    print(e)
                            else:
                                res = "The Value You Entered Does Not Exist, Try Again."
                        else:
                            res = "Invalid Value, Try Again."
                    else:
                        res = "Password Must Be 8 Characters At Least, Try Again."
                elif column != "Password" and condition_column == "Password":
                    if not val.isnumeric() and not condition_val.isnumeric():
                        hash_object = hashlib.md5(condition_val.encode())
                        condition_val = hash_object.hexdigest()
                        if Participants.objects.filter(**{condition_column: condition_val}).exists():
                            try:
                                Participants.objects.filter(**{condition_column: condition_val}).update(**{column: val})
                                res = "The Value Has Been Updated Successfully."
                            except IntegrityError as e:
                                res = "Error: " + str(e) + "."
                                print(e)
                        else:
                            res = "The Password You Entered Does Not Exist, Try Again."
                    else:
                        res = "Invalid Value, Try Again."
                elif column == "Password" and condition_column == "Password":
                    if len(val) >= 8 and len(condition_val) >= 8:
                        hash_object = hashlib.md5(val.encode())
                        val = hash_object.hexdigest()
                        hash_object = hashlib.md5(condition_val.encode())
                        condition_val = hash_object.hexdigest()
                        if Participants.objects.filter(**{condition_column: condition_val}).exists():
                            try:
                                Participants.objects.filter(**{condition_column: condition_val}).update(**{column: val})
                                res = "The Value Has Been Updated Successfully."
                            except IntegrityError as e:
                                res = "Error: " + str(e) + "."
                                print(e)
                        else:
                            res = "The Password You Entered Does Not Exist, Try Again."
                    else:
                        res = "Password Must Be 8 Characters At Least, Try Again."
        else:
            res = "Please, Enter The New Value."
        response += f"<h3>{res}</h3>"
        response += """
            </body>
            </html>
            """
    return HttpResponse(response)


def participantsDeletePy(request):
    response: str = ""
    response += """
        <!Doctype html>
        <html lang = 'en'>
        <head>
        <meta charset = 'utf-8'>
        <title>Participants Delete</title>
        </head>
        <body>
        <h1>Request Result</h1>
        """
    column = request.GET["col"]
    column = html.escape(column)
    if column is not None:
        res: str = ""
        val = request.GET["val"]
        val = html.escape(val)
        if column == "ParticipateID":
            try:
                val = int(val)
                try:
                    participant = Participants.objects.get(ParticipateID=val)
                    participant.delete()
                    res = "The Record Has Been Deleted Successfully."
                except Participants.DoesNotExist:
                    res = "The Participant ID You Entered Does Not Exist, Try Again."
                except IntegrityError as e:
                    res = "Error: " + str(e) + "."
                    print(e)
            except ValueError:
                res = "Invalid ID Value, Try Again."
        elif column == "Password":
            if len(val) >= 8:
                hash_object = hashlib.md5(val.encode())
                val = hash_object.hexdigest()
                if Participants.objects.filter(Password=val).exists():
                    try:
                        Participants.objects.filter(Password=val).delete()
                        res = "The Record Has Been Deleted Successfully."
                    except IntegrityError as e:
                        res = "Error: " + str(e) + "."
                        print(e)
                else:
                    res = "The Password You Entered Does Not Exist, Try Again."
            else:
                res = "Password Must Be At Least 8 Characters, Try Again."
        else:
            if not val.isnumeric():
                if Participants.objects.filter(**{column: val}).exists():
                    try:
                        Participants.objects.filter(**{column: val}).delete()
                        res = "The Record Has Been Deleted Successfully."
                    except IntegrityError as e:
                        res = "Error: " + str(e) + "."
                        print(e)
                else:
                    res = "The Value You Entered Does Not Exist, Try Again."
            else:
                res = "Invalid Value, Try Again."
        response += f"<h3>{res}</h3>"
        response += """
            </body>
            </html>
            """
    return HttpResponse(response)


def teachersInputsPy(request):
    response: str = ""
    response += """
        <!Doctype html>
        <html lang = 'en'>
        <head>
        <meta charset = 'utf-8'>
        <title>Participants Inputs</title>
        </head>
        <body>
        <h1>Request Result</h1>
        """
    teacherID = request.GET["teacherID"]
    participateID = request.GET["participateID"]
    subjectCode = request.GET["subjectCode"]
    teacherFirstName = request.GET["teacherFirstName"]
    teacherLastName = request.GET["teacherLastName"]
    teacherEmail = request.GET["teacherEmail"]
    teacherPassword = request.GET["teacherPassword"]
    teacherID = html.escape(teacherID)
    participateID = html.escape(participateID)
    subjectCode = html.escape(subjectCode)
    teacherFirstName = html.escape(teacherFirstName)
    teacherLastName = html.escape(teacherLastName)
    teacherEmail = html.escape(teacherEmail)
    teacherPassword = html.escape(teacherPassword)
    hash_object = hashlib.md5(teacherPassword.encode())
    teacherPassword = hash_object.hexdigest()
    if len(teacherID) != 0 and len(participateID) != 0 and len(subjectCode) != 0 \
            and len(teacherFirstName) != 0 and len(teacherLastName) != 0 and len(teacherEmail) != 0 \
            and len(teacherPassword) != 0:
        res: str = ""
        if teacherFirstName.isnumeric() or teacherLastName.isnumeric() or \
                teacherFirstName[0].isdigit() or teacherLastName[0].isdigit() or teacherEmail.isnumeric():
            res = "Please, Enter A Valid First And Last Name And Email."
        else:
            try:
                Teachers.objects.create(
                    TeacherID=teacherID,
                    ParticipateID=Participants.objects.get(pk=participateID),
                    SubjectCode=Subjects.objects.get(pk=subjectCode),
                    Firstname=teacherFirstName,
                    Lastname=teacherLastName,
                    Email=teacherEmail,
                    Password=teacherPassword
                )
                res = "Teacher Added Successfully."
            except IntegrityError as e:
                if 'UNIQUE constraint failed' in str(e):
                    res = "Teacher ID You Entered Already Exists, Try Again."
                else:
                    res = "Error: " + str(e) + "."
            except Participants.DoesNotExist as e:
                res = "Participate ID You Entered Does Not Exist, Try Again."
                print(e)
            except Subjects.DoesNotExist as e:
                res = "Subject Code You Entered Does Not Exist, Try Again."
                print(e)
        response += f"<h3>{res}</h3>"
        response += """
        </body>
        </html>
        """
    return HttpResponse(response)


def teachersOutputsPy(request):
    response: str = ""
    response += """
        <!Doctype html>
        <html lang = 'en'>
        <head>
        <meta charset = 'utf-8'>
        <title>Teachers Outputs</title>
        </head>
        <body>
        <h1>Outputs</h1>
        """
    data = Teachers.objects.all()
    response += "<table border = 1>\n"
    flag = True
    i = 0
    for teacher in data:
        response += "<tr>"
        if flag:
            response += """
            <th> Teacher ID </th>
            <th> Participate ID </th>
            <th> Subject Code </th>
            <th> First Name </th>
            <th> Last Name </th>
            <th> Email </th>
            <th> Password </th>
            </tr>
            """
            flag = False
        response += f"""      
          <th> {teacher.TeacherID} </th>
          <th> {teacher.ParticipateID} </th>
          <th> {teacher.SubjectCode} </th>
          <th> {teacher.Firstname} </th>
          <th> {teacher.Lastname} </th>
          <th> {teacher.Email} </th>
          <th> {teacher.Password} </th>
        """
        response += "</tr>"
        i += 1
    res = f"There Are {i} Teachers\n" if i > 0 else "No Teachers."
    response += "</table>"
    response += f"""
    {res}
    </body>
    </html>
    """
    return HttpResponse(response)


def teachersUpdatesPy(request):
    response: str = ""
    response += """
        <!Doctype html>
        <html lang = 'en'>
        <head>
        <meta charset = 'utf-8'>
        <title>Teachers Updates</title>
        </head>
        <body>
        <h1>Request Result</h1>
        """
    column = request.GET["col"]
    column = html.escape(column)
    if column is not None:
        res: str = ""
        val = request.GET["val"]
        val = html.escape(val)
        condition_column = request.GET["condition_col"]
        condition_column = html.escape(condition_column)
        if val is not None:
            if condition_column == "":
                if column == "ParticipateID" or column == "SubjectCode":
                    try:
                        val = int(val)
                        try:
                            Teachers.objects.all().update(**{column: val})
                            res = "The Value Has Been Updated Successfully for all Teachers."
                        except IntegrityError as e:
                            res = "Error: " + str(e) + "."
                            print(e)
                    except ValueError:
                        res = "Invalid Participate ID Or Subject Code Value, Try Again."
                elif column == "Password":
                    if len(val) >= 8:
                        hash_object = hashlib.md5(val.encode())
                        val = hash_object.hexdigest()
                        try:
                            Teachers.objects.all().update(Password=val)
                            res = "The Password Has Been Updated Successfully for all Teachers."
                        except IntegrityError as e:
                            res = "Error: " + str(e) + "."
                            print(e)
                    else:
                        res = "Password Must Be 8 Characters At Least, Try Again."
                else:
                    if not val.isnumeric():
                        try:
                            Teachers.objects.all().update(**{column: val})
                            res = "The Value Has Been Updated Successfully for all Teachers."
                        except IntegrityError as e:
                            res = "Error: " + str(e) + "."
                            print(e)
                    else:
                        res = "Invalid Value, Try Again."
            else:
                condition_val = request.GET["condition_val"]
                condition_val = html.escape(condition_val)
                if column in ["ParticipateID", "SubjectCode"] \
                        and condition_column in ["TeacherID", "ParticipateID", "SubjectCode"]:
                    try:
                        val = int(val)
                        condition_val = int(condition_val)
                        if Teachers.objects.filter(**{condition_column: condition_val}).exists():
                            try:
                                Teachers.objects.filter(**{condition_column: condition_val}).update(**{column: val})
                                res = "The Value Has Been Updated Successfully."
                            except IntegrityError as e:
                                res = "Error: " + str(e) + "."
                                print(e)
                        else:
                            res = "The Value You Entered Does Not Exist, Try Again."
                    except ValueError:
                        res = "Invalid Teacher ID, Participate ID Or Subject Code Value, Try Again."
                elif column in ["ParticipateID", "SubjectCode"] \
                        and condition_column not in ["TeacherID", "ParticipateID", "SubjectCode", "Password"]:
                    try:
                        val = int(val)
                        if not condition_val.isnumeric():
                            if Teachers.objects.filter(**{condition_column: condition_val}).exists():
                                try:
                                    Teachers.objects.filter(**{condition_column: condition_val}).update(**{column: val})
                                    res = "The Value Has Been Updated Successfully."
                                except IntegrityError as e:
                                    res = "Error: " + str(e) + "."
                                    print(e)
                            else:
                                res = "The Value You Entered Does Not Exist, Try Again."
                    except ValueError:
                        res = "Invalid Teacher ID, Participate ID Or Subject Code Value, Try Again."
                        if condition_val.isnumeric():
                            response += "<h3>Invalid Value, Try Again.</h3>"
                elif column in ["ParticipateID", "SubjectCode"] and condition_column == "Password":
                    if len(condition_val) >= 8:
                        try:
                            val = int(val)
                            if not condition_val.isnumeric():
                                hash_object = hashlib.md5(condition_val.encode())
                                condition_val = hash_object.hexdigest()
                                if Teachers.objects.filter(Password=condition_val).exists():
                                    try:
                                        Teachers.objects.filter(Password=condition_val).update(**{column: val})
                                        res = "The Value Has Been Updated Successfully."
                                    except IntegrityError as e:
                                        res = "Error: " + str(e) + "."
                                        print(e)
                                else:
                                    res = "The Password You Entered Does Not Exist, Try Again."
                        except ValueError:
                            res = "Invalid Participate ID Or Subject Code Value, Try Again."
                    else:
                        res = "Password Must Be 8 Characters At Least, Try Again."
                elif column not in ["ParticipateID", "SubjectCode"] and condition_column == "Password":
                    if len(condition_val) >= 8:
                        if not val.isnumeric() and not condition_val.isnumeric():
                            hash_object = hashlib.md5(condition_val.encode())
                            condition_val = hash_object.hexdigest()
                            if Teachers.objects.filter(Password=condition_val).exists():
                                try:
                                    Teachers.objects.filter(Password=condition_val).update(**{column: val})
                                    res = "The Value Has Been Updated Successfully."
                                except IntegrityError as e:
                                    res = "Error: " + str(e) + "."
                                    print(e)
                            else:
                                res = "The Password You Entered Does Not Exist, Try Again."
                        else:
                            res = "Invalid Value, Try Again."
                    else:
                        res = "Password Must Be 8 Characters At Least, Try Again."
                elif column not in ["ParticipateID", "SubjectCode", "Password"] \
                        and condition_column in ["TeacherID", "ParticipateID", "SubjectCode"]:
                    if not val.isnumeric():
                        try:
                            condition_val = int(condition_val)
                            if Teachers.objects.filter(**{condition_column: condition_val}).exists():
                                try:
                                    Teachers.objects.filter(**{condition_column: condition_val}).update(**{column: val})
                                    res = "The Value Has Been Updated Successfully."
                                except IntegrityError as e:
                                    res = "Error: " + str(e) + "."
                                    print(e)
                            else:
                                res = "The Value You Entered Does Not Exist, Try Again."
                        except ValueError:
                            res = "Invalid Teacher ID, Participate ID Or Subject Code Value, Try Again."
                    else:
                        res = "Invalid Value, Try Again."
                elif column == "Password" and condition_column in ["TeacherID", "ParticipateID", "SubjectCode"]:
                    if len(val) >= 8:
                        hash_object = hashlib.md5(val.encode())
                        val = hash_object.hexdigest()
                        try:
                            condition_val = int(condition_val)
                            if Teachers.objects.filter(**{condition_column: condition_val}).exists():
                                try:
                                    Teachers.objects.filter(**{condition_column: condition_val}).update(Password=val)
                                    res = "The Password Has Been Updated Successfully."
                                except IntegrityError as e:
                                    res = "Error: " + str(e) + "."
                                    print(e)
                            else:
                                res = "The Value You Entered Does Not Exist, Try Again."
                        except ValueError:
                            res = "Invalid Teacher ID, Participate ID Or Subject Code Value, Try Again."
                    else:
                        res = "Password Must Be 8 Characters At Least, Try Again."
                elif column == "Password" and condition_column not in ["TeacherID", "ParticipateID", "SubjectCode"]:
                    if len(val) >= 8:
                        hash_object = hashlib.md5(val.encode())
                        val = hash_object.hexdigest()
                        if not condition_val.isnumeric():
                            if Teachers.objects.filter(**{condition_column: condition_val}).exists():
                                try:
                                    Teachers.objects.filter(**{condition_column: condition_val}).update(Password=val)
                                    res = "The Password Has Been Updated Successfully."
                                except IntegrityError as e:
                                    res = "Error: " + str(e) + "."
                                    print(e)
                            else:
                                res = "The Value You Entered Does Not Exist, Try Again."
                        else:
                            res = "Invalid Value, Try Again."
                    else:
                        res = "Password Must Be 8 Characters At Least, Try Again."
                elif column not in ["ParticipateID", "SubjectCode", "Password"] \
                        and condition_column not in ["TeacherID", "ParticipateID", "SubjectCode", "Password"]:
                    if not val.isnumeric() and not condition_val.isnumeric():
                        if Teachers.objects.filter(**{condition_column: condition_val}).exists():
                            try:
                                Teachers.objects.filter(**{condition_column: condition_val}).update(**{column: val})
                                res = "The Value Has Been Updated Successfully."
                            except IntegrityError as e:
                                res = "Error: " + str(e) + "."
                                print(e)
                        else:
                            res = "The Value You Entered Does Not Exist, Try Again."
                    else:
                        res = "Invalid Value, Try Again."
                elif column == "Password" and condition_column == "Password":
                    if len(val) >= 8 and len(condition_val) >= 8:
                        hash_object = hashlib.md5(val.encode())
                        val = hash_object.hexdigest()
                        hash_object = hashlib.md5(condition_val.encode())
                        condition_val = hash_object.hexdigest()
                        if Teachers.objects.filter(Password=condition_val).exists():
                            try:
                                Teachers.objects.filter(Password=condition_val).update(Password=val)
                                res = "The Password Has Been Updated Successfully."
                            except IntegrityError as e:
                                res = "Error: " + str(e) + "."
                                print(e)
                        else:
                            res = "The Password You Entered Does Not Exist, Try Again."
                    else:
                        res = "Please, Check The Password You Entered (8 Characters At Least), Try Again."
        else:
            res = "Please, Enter The New Value."
        response += f"<h3>{res}</h3>"
        response += """
            </body>
            </html>
            """
    return HttpResponse(response)


def teachersDeletePy(request):
    response: str = ""
    response += """
        <!Doctype html>
        <html lang = 'en'>
        <head>
        <meta charset = 'utf-8'>
        <title>Teachers Delete</title>
        </head>
        <body>
        <h1>Request Result</h1>
        """
    column = request.GET["col"]
    column = html.escape(column)
    if column is not None:
        res: str = ""
        val = request.GET["val"]
        val = html.escape(val)
        if column == "TeacherID" or column == "ParticipateID" or column == "SubjectCode":
            try:
                val = int(val)
                if Teachers.objects.filter(**{column: val}).exists():
                    try:
                        Teachers.objects.filter(**{column: val}).delete()
                        res = "The Record Has Been Deleted Successfully."
                    except IntegrityError as e:
                        res = "Error: " + str(e) + "."
                        print(e)
                else:
                    res = "The Value You Entered Does Not Exist, Try Again."
            except ValueError:
                res = "Invalid Participate ID Or Subject Code Value, Try Again."
        elif column == "Password":
            if len(val) >= 8:
                hash_object = hashlib.md5(val.encode())
                val = hash_object.hexdigest()
                if Teachers.objects.filter(Password=val).exists():
                    try:
                        Teachers.objects.filter(Password=val).delete()
                        res = "The Record Has Been Deleted Successfully."
                    except IntegrityError as e:
                        res = "Error: " + str(e) + "."
                        print(e)
                else:
                    res = "The Password You Entered Does Not Exist, Try Again."
            else:
                res = "Password Must Be At Least 8 Characters, Try Again."
        else:
            if not val.isnumeric():
                if Teachers.objects.filter(**{column: val}).exists():
                    try:
                        Teachers.objects.filter(**{column: val}).delete()
                        res = "The Record Has Been Deleted Successfully."
                    except IntegrityError as e:
                        res = "Error: " + str(e) + "."
                        print(e)
                else:
                    res = "The Value You Entered Does Not Exist, Try Again."
            else:
                res = "Invalid Value, Try Again."
        response += f"<h3>{res}</h3>"
        response += """
            </body>
            </html>
            """
    return HttpResponse(response)


def subjectsInputsPy(request):
    response: str = ""
    response += """
        <!Doctype html>
        <html lang = 'en'>
        <head>
        <meta charset = 'utf-8'>
        <title>Subjects Inputs</title>
        </head>
        <body>
        <h1>Request Result</h1>
        """
    participateID = request.GET["participateID"]
    subjectCode = request.GET["subjectCode"]
    subjectName = request.GET["subjectName"]
    participateID = html.escape(participateID)
    subjectCode = html.escape(subjectCode)
    subjectName = html.escape(subjectName)
    if participateID is not None and subjectCode is not None and subjectName is not None:
        res: str = ""
        if subjectName.isnumeric() or subjectName[0].isdigit():
            res = "Please, Enter A Valid Subject Name."
        else:
            try:
                Subjects.objects.create(
                    ParticipateID=Participants.objects.get(pk=participateID),
                    SubjectCode=subjectCode,
                    SubjectName=subjectName
                )
                res = "The Subject Has Been Added Successfully."
            except IntegrityError as e:
                res = "Error: " + str(e) + "."
                print(e)
                if 'unique constraint failed' in str(e):
                    res = "Subject Code You Entered Already Exists, Try Again."
            except Participants.DoesNotExist as e:
                res = "Participate ID You Entered Does Not Exist, Try Again."
                print(e)
        response += f"<h3>{res}</h3>"
        response += """
        </body>
        </html>
        """
    return HttpResponse(response)


def subjectsOutputsPy(request):
    response: str = ""
    response += """
        <!Doctype html>
        <html lang = 'en'>
        <head>
        <meta charset = 'utf-8'>
        <title>Subjects Outputs</title>
        </head>
        <body>
        <h1>Outputs</h1>
        """
    data = Subjects.objects.all()
    response += "<table border = 1>\n"
    flag = True
    for subject in data:
        response += "<tr>"
        if flag:
            response += """
            <th> Participate ID </th>
            <th> Subject Code </th>
            <th> Subject Name </th>
            </tr>
            """
            flag = False
        response += f"""      
          <th> {subject.ParticipateID} </th>
          <th> {subject.SubjectCode} </th>
          <th> {subject.SubjectName} </th>
        """
        response += "</tr>"
    response += "</table>"
    response += """
    </body>
    </html>
    """
    return HttpResponse(response)


def subjectsUpdatesPy(request):
    response: str = ""
    response += """
        <!Doctype html>
        <html lang = 'en'>
        <head>
        <meta charset = 'utf-8'>
        <title>Subjects Updates</title>
        </head>
        <body>
        <h1>Request Result</h1>
        """
    column = request.GET["col"]
    column = html.escape(column)
    if column is not None:
        res: str = ""
        val = request.GET["val"]
        val = html.escape(val)
        condition_column = request.GET["condition_col"]
        condition_column = html.escape(condition_column)
        if val is not None:
            if condition_column == "":
                if column == "ParticipateID":
                    try:
                        val = int(val)
                        try:
                            Subjects.objects.all().update(**{column: val})
                            res = "The Value Has Been Updated Successfully for all Subjects."
                        except IntegrityError as e:
                            res = "Error: " + str(e) + "."
                            print(e)
                    except ValueError:
                        res = "Invalid Participate ID Value, Try Again."
                else:
                    if not val.isnumeric():
                        try:
                            Subjects.objects.all().update(**{column: val})
                            res = "The Value Has Been Updated Successfully for all Subjects."
                        except IntegrityError as e:
                            res = "Error: " + str(e) + "."
                            print(e)
                    else:
                        res = "Invalid Subject Value, Try Again."
            else:
                condition_val = request.GET["condition_val"]
                condition_val = html.escape(condition_val)
                if (column == "ParticipateID") \
                        and (condition_column == "ParticipateID" or condition_column == "SubjectCode"):
                    try:
                        val = int(val)
                        condition_val = int(condition_val)
                        if Subjects.objects.filter(**{condition_column: condition_val}).exists():
                            try:
                                Subjects.objects.filter(**{condition_column: condition_val}).update(**{column: val})
                                res = "The Value Has Been Updated Successfully."
                            except IntegrityError as e:
                                res = "Error: " + str(e) + "."
                                print(e)
                        else:
                            res = "The Value You Entered Does Not Exist, Try Again."
                    except ValueError:
                        res = "Invalid Participate ID Or Subject Code Value, Try Again."
                elif (column == "ParticipateID") \
                        and (condition_column != "ParticipateID" and condition_column != "SubjectCode"):
                    try:
                        val = int(val)
                        if not condition_val.isnumeric():
                            if Subjects.objects.filter(**{condition_column: condition_val}).exists():
                                try:
                                    Subjects.objects.filter(**{condition_column: condition_val}).update(**{column: val})
                                    res = "The Value Has Been Updated Successfully."
                                except IntegrityError as e:
                                    res = "Error: " + str(e) + "."
                                    print(e)
                            else:
                                res = "The Value You Entered Does Not Exist, Try Again."
                    except ValueError:
                        res = "Invalid Participate ID Or Subject Code Value, Try Again."
                        if condition_val.isnumeric():
                            response += "<h3>Invalid Subject Value, Try Again.</h3>"
                elif (column != "ParticipateID") \
                        and (condition_column == "ParticipateID" or condition_column == "SubjectCode"):
                    if not val.isnumeric():
                        try:
                            condition_val = int(condition_val)
                            if Subjects.objects.filter(**{condition_column: condition_val}).exists():
                                try:
                                    Subjects.objects.filter(**{condition_column: condition_val}).update(**{column: val})
                                    res = "The Value Has Been Updated Successfully."
                                except IntegrityError as e:
                                    res = "Error: " + str(e) + "."
                                    print(e)
                            else:
                                res = "The Value You Entered Does Not Exist, Try Again."
                        except ValueError:
                            res = "Invalid Participate ID Or Subject Code Value, Try Again."
                    else:
                        res = "Invalid Subject Value, Try Again."
                elif (column != "ParticipateID") \
                        and (condition_column != "ParticipateID" and condition_column != "SubjectCode"):
                    if not val.isnumeric() and not condition_val.isnumeric():

                        if Subjects.objects.filter(**{condition_column: condition_val}).exists():
                            try:
                                Subjects.objects.filter(**{condition_column: condition_val}).update(**{column: val})
                                res = "The Value Has Been Updated Successfully."
                            except IntegrityError as e:
                                res = "Error: " + str(e) + "."
                                print(e)
                        else:
                            res = "The Value You Entered Does Not Exist, Try Again."
                    else:
                        res = "Invalid Subject Value, Try Again."
        else:
            res = "Please, Enter The New Value."
        response += f"<h3>{res}</h3>"
        response += """
            </body>
            </html>
            """
    return HttpResponse(response)


def subjectsDeletePy(request):
    response: str = ""
    response += """
        <!Doctype html>
        <html lang = 'en'>
        <head>
        <meta charset = 'utf-8'>
        <title>Subjects Delete</title>
        </head>
        <body>
        <h1>Request Result</h1>
        """
    column = request.GET["col"]
    column = html.escape(column)
    if column is not None:
        res: str = ""
        val = request.GET["val"]
        val = html.escape(val)
        if column == "ParticipateID" or column == "SubjectCode":
            try:
                val = int(val)
                if Subjects.objects.filter(**{column: val}).exists():
                    try:
                        Subjects.objects.filter(**{column: val}).delete()
                        res = "The Record Has Been Deleted Successfully."
                    except IntegrityError as e:
                        res = "Error: " + str(e) + "."
                        print(e)
                else:
                    res = "The Value You Entered Does Not Exist, Try Again."
            except ValueError:
                res = "Invalid Participate ID Or Subject Code Value, Try Again."
        else:
            if not val.isnumeric():
                if Subjects.objects.filter(**{column: val}).exists():
                    try:
                        Subjects.objects.filter(**{column: val}).delete()
                        res = "The Record Has Been Deleted Successfully."
                    except IntegrityError as e:
                        res = "Error: " + str(e) + "."
                        print(e)
                else:
                    res = "The Value You Entered Does Not Exist, Try Again."
            else:
                res = "Invalid Subject Value, Try Again."
        response += f"<h3>{res}</h3>"
        response += """
            </body>
            </html>
            """
    return HttpResponse(response)


def progressRecordBookInputsPy(request):
    response: str = ""
    response += """
        <!Doctype html>
        <html lang = 'en'>
        <head>
        <meta charset = 'utf-8'>
        <title>Progress Record Book Inputs</title>
        </head>
        <body>
        <h1>Request Result</h1>
        """
    participateID = request.GET["participateID"]
    teacherID = request.GET["teacherID"]
    subjectCode = request.GET["subjectCode"]
    Rating = request.GET["Rating"]
    participateID = html.escape(participateID)
    teacherID = html.escape(teacherID)
    subjectCode = html.escape(subjectCode)
    Rating = html.escape(Rating)
    if participateID is not None and teacherID is not None and subjectCode is not None and Rating is not None:
        res: str = ""
        try:
            ProgessRecordBook.objects.create(
                ParticipateID=Participants.objects.get(pk=participateID),
                TeacherID=Teachers.objects.get(pk=teacherID),
                SubjectCode=Subjects.objects.get(pk=subjectCode),
                rating=Rating
            )
            res = "The Progress Record Has Been Added Successfully."
        except IntegrityError as e:
            if 'unique constraint failed' in str(e):
                res = "Participate ID, Teacher ID And Subject Code You Entered Are Already Exists, Try Again."
            else:
                res = "Error: " + str(e) + "."
        except Participants.DoesNotExist as e:
            res = "Participate ID You Entered Does Not Exist, Try Again."
            print(e)
        except Teachers.DoesNotExist as e:
            res = "Teacher ID You Entered Does Not Exist, Try Again."
            print(e)
        except Subjects.DoesNotExist as e:
            res = "Subject Code You Entered Does Not Exist, Try Again."
            print(e)
        response += f"<h3>{res}</h3>"
        response += """
        </body>
        </html>
        """
    return HttpResponse(response)


def progressRecordBookOutputsPy(request):
    response: str = ""
    response += """
        <!Doctype html>
        <html lang = 'en'>
        <head>
        <meta charset = 'utf-8'>
        <title>Progress Record Book Outputs</title>
        </head>
        <body>
        <h1>Outputs</h1>
        """
    data = ProgessRecordBook.objects.all()
    response += "<table border = 1>\n"
    flag = True
    for progress_record_book in data:
        response += "<tr>"
        if flag:
            response += """
            <th> Participate ID </th>
            <th> Teacher ID </th>
            <th> Subject Code </th>
            <th> Rating </th>
            </tr>
            """
            flag = False
        response += f"""      
          <th> {progress_record_book.ParticipateID} </th>
          <th> {progress_record_book.TeacherID} </th>
          <th> {progress_record_book.SubjectCode} </th>
          <th> {progress_record_book.rating} </th>
        """
        response += "</tr>"
    response += "</table>"
    response += """
    </body>
    </html>
    """
    return HttpResponse(response)


def progressRecordBookUpdatesPy(request):
    response: str = ""
    response += """
        <!Doctype html>
        <html lang = 'en'>
        <head>
        <meta charset = 'utf-8'>
        <title>Progress Record Book Updates</title>
        </head>
        <body>
        <h1>Request Result</h1>
        """
    column = request.GET["col"]
    column = html.escape(column)
    if column is not None:
        res: str = ""
        val = request.GET["val"]
        val = html.escape(val)
        condition_column = request.GET["condition_col"]
        condition_column = html.escape(condition_column)
        if val is not None:
            if condition_column == "":
                val = int(val)
                try:
                    ProgessRecordBook.objects.all().update(**{column: val})
                    res = "The Value Has Been Updated Successfully for all Progress Record Books."
                except IntegrityError as e:
                    res = "Error: " + str(e) + "."
                    print(e)
            else:
                condition_val = request.GET["condition_val"]
                condition_val = html.escape(condition_val)
                val = int(val)
                condition_val = int(condition_val)
                if ProgessRecordBook.objects.filter(**{condition_column: condition_val}).exists():
                    try:
                        ProgessRecordBook.objects.filter(**{condition_column: condition_val}).update(**{column: val})
                        res = "The Value Has Been Updated Successfully."
                    except IntegrityError as e:
                        res = "Error: " + str(e) + "."
                        print(e)
                else:
                    res = "The Value You Entered Does Not Exist, Try Again."
        else:
            res = "Please, Enter The New Value."
        response += f"<h3>{res}</h3>"
        response += """
            </body>
            </html>
            """
    return HttpResponse(response)


def progressRecordBookDeletePy(request):
    response: str = ""
    response += """
        <!Doctype html>
        <html lang = 'en'>
        <head>
        <meta charset = 'utf-8'>
        <title>Progress Record Book Delete</title>
        </head>
        <body>
        <h1>Request Result</h1>
        """
    column = request.GET["col"]
    column = html.escape(column)
    if column is not None:
        res: str = ""
        val = request.GET["val"]
        val = html.escape(val)
        val = int(val)
        if ProgessRecordBook.objects.filter(**{column: val}).exists():
            try:
                ProgessRecordBook.objects.filter(**{column: val}).delete()
                res = "The Record Has Been Deleted Successfully."
            except IntegrityError as e:
                res = "Error: " + str(e) + "."
                print(e)
        else:
            res = "The Value You Entered Does Not Exist, Try Again."
        response += f"<h3>{res}</h3>"
        response += """
            </body>
            </html>
            """
    return HttpResponse(response)


def feedbacksInputsPy(request):
    response: str = ""
    response += """
        <!Doctype html>
        <html lang = 'en'>
        <head>
        <meta charset = 'utf-8'>
        <title>Feedbacks Inputs</title>
        </head>
        <body>
        <h1>Request Result</h1>
        """
    participateID = request.GET["participateID"]
    feedback = request.GET["feedback"]
    participateID = html.escape(participateID)
    feedback = html.escape(feedback)
    if participateID is not None and feedback is not None:
        res: str = ""
        try:
            Feedbacks.objects.create(
                ParticipateID=Participants.objects.get(pk=participateID),
                Feedback=feedback
            )
            res = "The Feedback Has Been Added Successfully."
        except IntegrityError as e:
            res = "Error: " + str(e) + "."
            print(e)
            if 'unique constraint failed' in str(e):
                res = "Feedback ID You Entered Already Exists, Try Again."
        except Participants.DoesNotExist as e:
            res = "Participate ID You Entered Does Not Exist, Try Again."
            print(e)
        response += f"<h3>{res}</h3>"
        response += """
        </body>
        </html>
        """
    return HttpResponse(response)


def feedbacksOutputsPy(request):
    response: str = ""
    response += """
        <!Doctype html>
        <html lang = 'en'>
        <head>
        <meta charset = 'utf-8'>
        <title>Feedbacks Outputs</title>
        </head>
        <body>
        <h1>Outputs</h1>
        """
    data = Feedbacks.objects.all()
    response += "<table border = 1>\n"
    flag = True
    for feedback in data:
        response += "<tr>"
        if flag:
            response += """
            <th> Feedback ID </th>
            <th> Participate ID </th>
            <th> Feedback </th>
            </tr>
            """
            flag = False
        response += f"""      
          <th> {feedback.FeedbackID} </th>
          <th> {feedback.ParticipateID} </th>
          <th> {feedback.Feedback} </th>
        """
        response += "</tr>"
    response += "</table>"
    response += """
    </body>
    </html>
    """
    return HttpResponse(response)


def feedbacksUpdatesPy(request):
    response: str = ""
    response += """
        <!Doctype html>
        <html lang = 'en'>
        <head>
        <meta charset = 'utf-8'>
        <title>Feedbacks Updates</title>
        </head>
        <body>
        <h1>Request Result</h1>
        """
    column = request.GET["col"]
    column = html.escape(column)
    if column is not None:
        res: str = ""
        val = request.GET["val"]
        val = html.escape(val)
        condition_column = request.GET["condition_col"]
        condition_column = html.escape(condition_column)
        if val is not None:
            if condition_column == "":
                if column == "ParticipateID":
                    try:
                        val = int(val)
                        try:
                            Feedbacks.objects.all().update(**{column: val})
                            res = "The Value Has Been Updated Successfully for all Feedbacks."
                        except IntegrityError as e:
                            res = "Error: " + str(e) + "."
                            print(e)
                    except ValueError:
                        res = "Invalid Participate ID Value, Try Again."
                else:
                    if not val.isnumeric():
                        try:
                            Feedbacks.objects.all().update(**{column: val})
                            res = "The Value Has Been Updated Successfully for all Feedbacks."
                        except IntegrityError as e:
                            res = "Error: " + str(e) + "."
                            print(e)
                    else:
                        res = "Invalid Feedback Value, Try Again."
            else:
                condition_val = request.GET["condition_val"]
                condition_val = html.escape(condition_val)
                if (column == "ParticipateID") \
                        and (condition_column == "FeedbackID" or condition_column == "ParticipateID"):
                    try:
                        val = int(val)
                        condition_val = int(condition_val)
                        if Feedbacks.objects.filter(**{condition_column: condition_val}).exists():
                            try:
                                Feedbacks.objects.filter(**{condition_column: condition_val}).update(**{column: val})
                                res = "The Value Has Been Updated Successfully."
                            except IntegrityError as e:
                                res = "Error: " + str(e) + "."
                                print(e)
                        else:
                            res = "The Value You Entered Does Not Exist, Try Again."
                    except ValueError:
                        res = "Invalid Feedback ID or Participate ID Value, Try Again."
                elif (column == "ParticipateID") \
                        and (condition_column != "FeedbackID" and condition_column != "ParticipateID"):
                    try:
                        val = int(val)
                        if not condition_val.isnumeric():
                            if Feedbacks.objects.filter(**{condition_column: condition_val}).exists():
                                try:
                                    Feedbacks.objects.filter(**{condition_column: condition_val}).update(
                                        **{column: val})
                                    res = "The Value Has Been Updated Successfully."
                                except IntegrityError as e:
                                    res = "Error: " + str(e) + "."
                                    print(e)
                            else:
                                res = "The Value You Entered Does Not Exist, Try Again."
                    except ValueError:
                        res = "Invalid Feedback ID or Participate ID Value, Try Again."
                elif (column != "ParticipateID") \
                        and (condition_column == "FeedbackID" or condition_column == "ParticipateID"):
                    try:
                        condition_val = int(condition_val)
                        if Feedbacks.objects.filter(**{condition_column: condition_val}).exists():
                            try:
                                Feedbacks.objects.filter(**{condition_column: condition_val}).update(**{column: val})
                                res = "The Value Has Been Updated Successfully."
                            except IntegrityError as e:
                                res = "Error: " + str(e) + "."
                                print(e)
                        else:
                            res = "The Value You Entered Does Not Exist, Try Again."
                    except ValueError:
                        res = "Invalid Feedback ID or Participate ID Value, Try Again."
                elif (column != "ParticipateID") \
                        and (condition_column != "FeedbackID" and condition_column != "ParticipateID"):
                    if Feedbacks.objects.filter(**{condition_column: condition_val}).exists():
                        try:
                            Feedbacks.objects.filter(**{condition_column: condition_val}).update(**{column: val})
                            res = "The Value Has Been Updated Successfully."
                        except IntegrityError as e:
                            res = "Error: " + str(e) + "."
                            print(e)
                    else:
                        res = "The Value You Entered Does Not Exist, Try Again."
        else:
            res = "Please, Enter The New Value."
        response += f"<h3>{res}</h3>"
        response += """
            </body>
            </html>
            """
    return HttpResponse(response)


def feedbacksDeletePy(request):
    response: str = ""
    response += """
        <!Doctype html>
        <html lang = 'en'>
        <head>
        <meta charset = 'utf-8'>
        <title>Feedbacks Delete</title>
        </head>
        <body>
        <h1>Request Result</h1>
        """
    column = request.GET["col"]
    column = html.escape(column)
    if column is not None:
        res: str = ""
        val = request.GET["val"]
        val = html.escape(val)
        if column == "FeedbackID" or column == "ParticipateID":
            try:
                val = int(val)
                if Feedbacks.objects.filter(**{column: val}).exists():
                    try:
                        Feedbacks.objects.filter(**{column: val}).delete()
                        res = "The Record Has Been Deleted Successfully."
                    except IntegrityError as e:
                        res = "Error: " + str(e) + "."
                        print(e)
                else:
                    res = "The Value You Entered Does Not Exist, Try Again."
            except ValueError:
                res = "Invalid Feedback ID or Participate ID Value, Try Again."
        else:
            if Feedbacks.objects.filter(**{column: val}).exists():
                try:
                    Feedbacks.objects.filter(**{column: val}).delete()
                    res = "The Record Has Been Deleted Successfully."
                except IntegrityError as e:
                    res = "Error: " + str(e) + "."
                    print(e)
            else:
                res = "The Value You Entered Does Not Exist, Try Again."
        response += f"<h3>{res}</h3>"
        response += """
            </body>
            </html>
            """
    return HttpResponse(response)
