# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from loginSystem.views import loadLoginPage
from loginSystem.models import Administrator
import json
from .models import Package, VMPackage
import plogical.CyberCPLogFileWriter as logging
from plogical.acl import ACLManager

# Create your views here.


def packagesHome(request):
    try:
        val = request.session['userID']
        return render(request, 'packages/index.html', {})
    except KeyError:
        return redirect(loadLoginPage)

def createPacakge(request):

    try:
        userID = request.session['userID']
        admin = Administrator.objects.get(pk=userID)
        currentACL = ACLManager.loadedACL(userID)

        if currentACL['admin'] == 1:
            pass
        elif currentACL['createPackage'] == 1:
            pass
        else:
            return ACLManager.loadError()

        return render(request, 'packages/createPackage.html', {"admin": admin.userName})

    except KeyError:
        return redirect(loadLoginPage)

def deletePacakge(request):
    try:
        userID = request.session['userID']
        try:
            currentACL = ACLManager.loadedACL(userID)

            if currentACL['admin'] == 1:
                pass
            elif currentACL['deletePackage'] == 1:
                pass
            else:
                return ACLManager.loadError()

            packageList = ACLManager.loadPackages(userID, currentACL)
            return render(request, 'packages/deletePackage.html', {"packageList": packageList})

        except BaseException,msg:
            logging.CyberCPLogFileWriter.writeToFile(str(msg))
            return HttpResponse("Please see CyberCP Main Log File")
    except KeyError:
        return redirect(loadLoginPage)

def submitPackage(request):
    try:
        userID = request.session['userID']
        currentACL = ACLManager.loadedACL(userID)

        if currentACL['admin'] == 1:
            pass
        elif currentACL['createPackage'] == 1:
            pass
        else:
            return ACLManager.loadErrorJson('saveStatus', 0)
        try:
            if request.method == 'POST':
                data = json.loads(request.body)
                packageName = data['packageName']
                packageSpace = int(data['diskSpace'])
                packageBandwidth = int(data['bandwidth'])
                packageDatabases = int(data['dataBases'])
                ftpAccounts = int(data['ftpAccounts'])
                emails = int(data['emails'])
                allowedDomains = int(data['allowedDomains'])


                if packageSpace < 0 or packageBandwidth < 0 or packageDatabases < 0 or ftpAccounts < 0 or emails < 0 or allowedDomains < 0:
                    data_ret = {'saveStatus': 0, 'error_message': "All values should be positive or 0."}
                    json_data = json.dumps(data_ret)
                    return HttpResponse(json_data)

                admin = Administrator.objects.get(pk=userID)

                packageName = admin.userName + "_" + packageName

                package = Package(admin=admin, packageName=packageName, diskSpace=packageSpace,
                                  bandwidth=packageBandwidth, ftpAccounts=ftpAccounts, dataBases=packageDatabases,
                                  emailAccounts=emails, allowedDomains=allowedDomains)

                package.save()

                data_ret = {'saveStatus': 1, 'error_message': "None"}
                json_data = json.dumps(data_ret)
                return HttpResponse(json_data)

        except BaseException,msg:
            data_ret = {'saveStatus': 0, 'error_message': str(msg)}
            json_data = json.dumps(data_ret)
            return HttpResponse(json_data)
    except KeyError:
        return redirect(loadLoginPage)

def submitDelete(request):
    try:
        userID = request.session['userID']
        try:

            currentACL = ACLManager.loadedACL(userID)

            if currentACL['admin'] == 1:
                pass
            elif currentACL['deletePackage'] == 1:
                pass
            else:
                return ACLManager.loadErrorJson('deleteStatus', 0)

            if request.method == 'POST':
                data = json.loads(request.body)
                packageName = data['packageName']

                delPackage = Package.objects.get(packageName=packageName)
                delPackage.delete()

                data_ret = {'deleteStatus': 1, 'error_message': "None"}
                json_data = json.dumps(data_ret)
                return HttpResponse(json_data)

        except BaseException,msg:
            data_ret = {'deleteStatus': 0, 'error_message': str(msg)}
            json_data = json.dumps(data_ret)
            return HttpResponse(json_data)
    except KeyError,msg:
        data_ret = {'deleteStatus': 0, 'error_message': str(msg)}
        json_data = json.dumps(data_ret)
        return HttpResponse(json_data)

def modifyPackage(request):
    try:
        userID = request.session['userID']
        try:
            currentACL = ACLManager.loadedACL(userID)

            if currentACL['admin'] == 1:
                pass
            elif currentACL['modifyPackage'] == 1:
                pass
            else:
                return ACLManager.loadError()

            packageList = ACLManager.loadPackages(userID, currentACL)
            return render(request, 'packages/modifyPackage.html', {"packList": packageList})

        except BaseException,msg:
            logging.CyberCPLogFileWriter.writeToFile(str(msg))
            return HttpResponse("Please see CyberCP Main Log File")
    except KeyError:
        return redirect(loadLoginPage)

def submitModify(request):
    try:
        userID = request.session['userID']
        try:
            if request.method == 'POST':

                data = json.loads(request.body)
                packageName = data['packageName']

                currentACL = ACLManager.loadedACL(userID)

                if currentACL['admin'] == 1:
                    pass
                elif currentACL['modifyPackage'] == 1:
                    pass
                else:
                    return ACLManager.loadErrorJson('modifyStatus', 0)

                modifyPack = Package.objects.get(packageName=packageName)

                diskSpace = modifyPack.diskSpace
                bandwidth = modifyPack.bandwidth
                ftpAccounts = modifyPack.ftpAccounts
                dataBases = modifyPack.dataBases
                emails = modifyPack.emailAccounts

                data_ret = {'emails': emails, 'modifyStatus': 1, 'error_message': "None",
                            "diskSpace": diskSpace, "bandwidth": bandwidth, "ftpAccounts": ftpAccounts,
                            "dataBases": dataBases, "allowedDomains": modifyPack.allowedDomains}
                json_data = json.dumps(data_ret)
                return HttpResponse(json_data)


        except BaseException,msg:
            data_ret = {'modifyStatus': 0, 'error_message': str(msg)}
            json_data = json.dumps(data_ret)
            return HttpResponse(json_data)

    except KeyError,msg:
        data_ret = {'modifyStatus': 0, 'error_message': str(msg)}
        json_data = json.dumps(data_ret)
        return HttpResponse(json_data)

def saveChanges(request):
    try:
        userID = request.session['userID']
        try:
            if request.method == 'POST':
                data = json.loads(request.body)
                packageName = data['packageName']

                currentACL = ACLManager.loadedACL(userID)

                if currentACL['admin'] == 1:
                    pass
                elif currentACL['modifyPackage'] == 1:
                    pass
                else:
                    return ACLManager.loadErrorJson('saveStatus', 0)

                if data['diskSpace'] < 0 or data['bandwidth'] < 0 or data['ftpAccounts'] < 0 or data['dataBases'] < 0 or \
                                data['emails'] < 0 or data['allowedDomains'] < 0:
                    data_ret = {'saveStatus': 0, 'error_message': "All values should be positive or 0."}
                    json_data = json.dumps(data_ret)
                    return HttpResponse(json_data)

                modifyPack = Package.objects.get(packageName=packageName)

                modifyPack.diskSpace = data['diskSpace']
                modifyPack.bandwidth = data['bandwidth']
                modifyPack.ftpAccounts = data['ftpAccounts']
                modifyPack.dataBases = data['dataBases']
                modifyPack.emailAccounts = data['emails']
                modifyPack.allowedDomains = data['allowedDomains']
                modifyPack.save()

                data_ret = {'saveStatus': 1, 'error_message': "None"}
                json_data = json.dumps(data_ret)
                return HttpResponse(json_data)

        except BaseException,msg:
            data_ret = {'saveStatus': 0, 'error_message': str(msg)}
            json_data = json.dumps(data_ret)
            return HttpResponse(json_data)

    except KeyError,msg:
        data_ret = {'saveStatus': 0, 'error_message': str(msg)}
        json_data = json.dumps(data_ret)
        return HttpResponse(json_data)


##

def packagesHomeVMM(request):
    try:
        val = request.session['userID']
        return render(request, 'packages/indexVMM.html', {})
    except KeyError:
        return redirect(loadLoginPage)

def createPacakgeVMM(request):
    try:
        val = request.session['userID']

        admin = Administrator.objects.get(pk=val)

        if admin.type == 3:
            return HttpResponse("You don't have enough privileges to access this page.")

    except KeyError:
        return redirect(loadLoginPage)

    return render(request,'packages/createPackageVMM.html',{"admin":admin.userName})

def deletePacakgeVMM(request):

    try:
        val = request.session['userID']
        try:

            admin = Administrator.objects.get(pk=val)

            if admin.type == 3:
                return HttpResponse("You don't have enough privileges to access this page.")

            if admin.type == 1:
                packages = VMPackage.objects.all()
            else:
                packages = VMPackage.objects.filter(admin=admin)

            packageList = []
            for items in packages:
                packageList.append(items.packageName)

        except BaseException,msg:
            logging.CyberCPLogFileWriter.writeToFile(str(msg))
            return HttpResponse("Please see CyberCP Main Log File")

    except KeyError:
        return redirect(loadLoginPage)

    return render(request,'packages/deletePackageVMM.html',{"packageList" : packageList})

def submitPackageVMM(request):
    try:
        val = request.session['userID']
        try:
            if request.method == 'POST':
                data = json.loads(request.body)
                packageName = data['packageName']
                diskSpace = data['diskSpace']
                guaranteedRam = data['guaranteedRam']
                bandwidth = data['bandwidth']
                cpuCores = data['cpuCores']

                admin = Administrator.objects.get(pk=request.session['userID'])

                packageName = packageName

                package = VMPackage(admin=admin,
                                  packageName=packageName,
                                  diskSpace=diskSpace,
                                  guaranteedRam=guaranteedRam,
                                  bandwidth=bandwidth,
                                  cpuCores=cpuCores,
                                  )

                package.save()

                data_ret = {'success': 1,'error_message': "None", 'successMessage': 'Package successfully created!'}
                json_data = json.dumps(data_ret)
                return HttpResponse(json_data)

        except BaseException,msg:
            data_ret = {'success': 0, 'error_message': str(msg)}
            json_data = json.dumps(data_ret)
            return HttpResponse(json_data)
    except KeyError:
        return redirect(loadLoginPage)

def submitDeleteVMM(request):
    try:
        val = request.session['userID']
        try:
            if request.method == 'POST':
                data = json.loads(request.body)
                packageName = data['packageName']

                delPackage = VMPackage.objects.get(packageName=packageName)
                delPackage.delete()

                data_ret = {'deleteStatus': 1,'error_message': "None"}
                json_data = json.dumps(data_ret)
                return HttpResponse(json_data)

        except BaseException,msg:
            data_ret = {'deleteStatus': 0, 'error_message': str(msg)}
            json_data = json.dumps(data_ret)
            return HttpResponse(json_data)
    except KeyError,msg:
        data_ret = {'deleteStatus': 0, 'error_message': str(msg)}
        json_data = json.dumps(data_ret)
        return HttpResponse(json_data)

def modifyPackageVMM(request):
    try:
        val = request.session['userID']
        try:
            admin = Administrator.objects.get(pk=val)

            if admin.type == 3:
                return HttpResponse("You don't have enough privileges to access this page.")

            if admin.type == 1:
                packages = VMPackage.objects.all()
            else:
                packages = VMPackage.objects.filter(admin=admin)

            packageList = []
            for items in packages:
                packageList.append(items.packageName)
            return render(request, 'packages/modifyPackageVMM.html', {"packList": packageList})

        except BaseException,msg:
            logging.CyberCPLogFileWriter.writeToFile(str(msg))
            return HttpResponse("Please see CyberCP Main Log File")
    except KeyError:
        return redirect(loadLoginPage)

def submitModifyVMM(request):
    try:
        val = request.session['userID']
        try:
            if request.method == 'POST':

                data = json.loads(request.body)
                packageName = data['packageName']

                modifyPack = VMPackage.objects.get(packageName=packageName)

                diskSpace = modifyPack.diskSpace
                guaranteedRam = modifyPack.guaranteedRam
                bandwidth = modifyPack.bandwidth
                cpuCores = modifyPack.cpuCores

                data_ret = {'modifyStatus': 1,
                            'error_message': "None",
                            'packageName' : packageName,
                            'diskSpace':diskSpace,
                            'guaranteedRam':guaranteedRam,
                            'bandwidth': bandwidth,
                            'cpuCores': cpuCores,
                            }
                json_data = json.dumps(data_ret)
                return HttpResponse(json_data)

        except BaseException,msg:
            data_ret = {'modifyStatus': 0, 'error_message': str(msg)}
            json_data = json.dumps(data_ret)
            return HttpResponse(json_data)

    except KeyError,msg:
        data_ret = {'modifyStatus': 0, 'error_message': str(msg)}
        json_data = json.dumps(data_ret)
        return HttpResponse(json_data)

def saveChangesVMM(request):
    try:
        val = request.session['userID']
        try:
            if request.method == 'POST':

                data = json.loads(request.body)
                packageName = data['packageName']

                modifyPack = VMPackage.objects.get(packageName=packageName)

                modifyPack.diskSpace = data['diskSpace']
                modifyPack.bandwidth = data['bandwidth']
                modifyPack.guaranteedRam = data['guaranteedRam']
                modifyPack.cpuCores = data['cpuCores']
                modifyPack.save()

                data_ret = {'saveStatus': 1,'error_message': "None"}
                json_data = json.dumps(data_ret)
                return HttpResponse(json_data)

        except BaseException,msg:
            data_ret = {'saveStatus': 0, 'error_message': str(msg)}
            json_data = json.dumps(data_ret)
            return HttpResponse(json_data)

    except KeyError,msg:
        data_ret = {'saveStatus': 0, 'error_message': str(msg)}
        json_data = json.dumps(data_ret)
        return HttpResponse(json_data)