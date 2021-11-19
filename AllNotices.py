from FetchNotices import getNoticesFromBaseUrl
import json
baseurl = 'https://nitdgp.ac.in/p/noticesnitd/'
general = baseurl + 'general-2'
academic = baseurl + 'academic-2'
student = baseurl + 'student-1'
hostel = baseurl + 'hostel'
covid19 = baseurl + 'covid-19'
scholarship = baseurl + 'scholarship'

generalNotices = {"General":getNoticesFromBaseUrl(general)}
academicNotices = {"Academic":getNoticesFromBaseUrl(academic)}
studentNotices = {"Student": getNoticesFromBaseUrl(student)}
hostelNotices = {"Hostel": getNoticesFromBaseUrl(hostel)}
covid19Notices = {"Covid":getNoticesFromBaseUrl(covid19)}
scholarshipNotices = {"Scholarship": getNoticesFromBaseUrl(scholarship)}
AllNotices = {}

AllNotices.update(generalNotices)
AllNotices.update(academicNotices)
AllNotices.update(studentNotices)
AllNotices.update(hostelNotices)
AllNotices.update(covid19Notices)
AllNotices.update(scholarshipNotices)




print(json.dumps(AllNotices,indent=2))