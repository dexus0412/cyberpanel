# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from loginSystem.models import Administrator
from loginSystem.views import loadLoginPage
import plogical.CyberCPLogFileWriter as logging
import json
from plogical.website import WebsiteManager

def loadWebsitesHome(request):
    try:
        val = request.session['userID']
        admin = Administrator.objects.get(pk=val)
        return render(request,'websiteFunctions/index.html',{"type":admin.type})
    except KeyError:
        return redirect(loadLoginPage)

def createWebsite(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.createWebsite(request, userID)
    except KeyError:
        return redirect(loadLoginPage)

def modifyWebsite(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.modifyWebsite(request, userID)
    except BaseException, msg:
        return HttpResponse(str(msg))

    except KeyError:
        return redirect(loadLoginPage)

def deleteWebsite(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.deleteWebsite(request, userID)
    except KeyError:
        return redirect(loadLoginPage)

def siteState(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.siteState(request, userID)
    except KeyError:
        return redirect(loadLoginPage)

def listWebsites(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.listWebsites(request, userID)
    except KeyError:
        return redirect(loadLoginPage)

def submitWebsiteCreation(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.submitWebsiteCreation(userID, json.loads(request.body))
    except KeyError:
        return redirect(loadLoginPage)

def submitDomainCreation(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.submitDomainCreation(userID, json.loads(request.body))
    except KeyError:
        return redirect(loadLoginPage)

def fetchDomains(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.fetchDomains(userID, json.loads(request.body))
    except KeyError:
        return redirect(loadLoginPage)

def getFurtherAccounts(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.getFurtherAccounts(userID, json.loads(request.body))
    except KeyError:
        return redirect(loadLoginPage)

def submitWebsiteDeletion(request):
    try:

        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.submitWebsiteDeletion(userID, json.loads(request.body))

    except KeyError:
        return redirect(loadLoginPage)

def submitDomainDeletion(request):
    try:

        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.submitDomainDeletion(userID, json.loads(request.body))

    except KeyError:
        return redirect(loadLoginPage)

def submitWebsiteStatus(request):
    try:

        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.submitWebsiteStatus(userID, json.loads(request.body))

    except KeyError:
        return redirect(loadLoginPage)

def submitWebsiteModify(request):
    try:

        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.submitWebsiteModify(userID, json.loads(request.body))

    except KeyError:
        return redirect(loadLoginPage)

def saveWebsiteChanges(request):
    try:

        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.saveWebsiteChanges(userID, json.loads(request.body))

    except KeyError:
        return redirect(loadLoginPage)

def domain(request, domain):
    try:

        userID = request.session['userID']
        wm = WebsiteManager(domain)
        return wm.loadDomainHome(request, userID)

    except KeyError:
        return redirect(loadLoginPage)

def launchChild(request, domain, childDomain):
    try:
        userID = request.session['userID']
        wm = WebsiteManager(domain, childDomain)
        return wm.launchChild(request, userID)
    except KeyError:
        return redirect(loadLoginPage)

def getDataFromLogFile(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.getDataFromLogFile(userID, json.loads(request.body))
    except KeyError:
        return redirect(loadLoginPage)

def fetchErrorLogs(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.fetchErrorLogs(userID, json.loads(request.body))
    except KeyError:
        return redirect(loadLoginPage)

def getDataFromConfigFile(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.getDataFromConfigFile(userID, json.loads(request.body))
    except KeyError:
        return redirect(loadLoginPage)

def saveConfigsToFile(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.saveConfigsToFile(userID, json.loads(request.body))
    except KeyError:
        return redirect(loadLoginPage)

def getRewriteRules(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.getRewriteRules(userID, json.loads(request.body))
    except KeyError:
        return redirect(loadLoginPage)

def saveRewriteRules(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.saveRewriteRules(userID, json.loads(request.body))
    except KeyError:
        return redirect(loadLoginPage)

def saveSSL(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.saveSSL(userID, json.loads(request.body))
    except KeyError:
        return redirect(loadLoginPage)

def changePHP(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.changePHP(userID, json.loads(request.body))
    except KeyError:
        return redirect(loadLoginPage)

def listCron(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.listCron(request, userID)
    except KeyError:
        return redirect(loadLoginPage)

def getWebsiteCron(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.getWebsiteCron(userID, json.loads(request.body))
    except KeyError:
        return redirect(loadLoginPage)

def getCronbyLine(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.getCronbyLine(userID, json.loads(request.body))
    except KeyError:
        return redirect(loadLoginPage)

def saveCronChanges(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.saveCronChanges(userID, json.loads(request.body))
    except KeyError:
        return redirect(loadLoginPage)

def remCronbyLine(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.remCronbyLine(userID, json.loads(request.body))
    except KeyError:
        return redirect(loadLoginPage)

def addNewCron(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.addNewCron(userID, json.loads(request.body))
    except KeyError:
        return redirect(loadLoginPage)

def domainAlias(request, domain):
    try:
        userID = request.session['userID']
        wm = WebsiteManager(domain)
        return wm.domainAlias(request, userID)
    except KeyError:
        return redirect(loadLoginPage)

def submitAliasCreation(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.submitAliasCreation(userID, json.loads(request.body))
    except KeyError:
        return redirect(loadLoginPage)

def issueAliasSSL(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.issueAliasSSL(userID, json.loads(request.body))
    except KeyError:
        return redirect(loadLoginPage)

def delateAlias(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.delateAlias(userID, json.loads(request.body))
    except KeyError:
        return redirect(loadLoginPage)

def changeOpenBasedir(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.changeOpenBasedir(userID, json.loads(request.body))
    except KeyError:
        return redirect(loadLoginPage)

def applicationInstaller(request):
    try:
        userID = request.session['userID']
        try:
            return render(request, 'websiteFunctions/applicationInstaller.html')
        except BaseException, msg:
            logging.CyberCPLogFileWriter.writeToFile(str(msg))
            return HttpResponse(str(msg))
    except KeyError:
        return redirect(loadLoginPage)

def wordpressInstall(request, domain):
    try:
        userID = request.session['userID']
        wm = WebsiteManager(domain)
        return wm.wordpressInstall(request, userID)
    except KeyError:
        return redirect(loadLoginPage)

def installWordpress(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.installWordpress(userID, json.loads(request.body))
    except KeyError:
        return redirect(loadLoginPage)

def installWordpressStatus(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.installWordpressStatus(userID, json.loads(request.body))
    except KeyError:
        return redirect(loadLoginPage)

def joomlaInstall(request, domain):
    try:
        userID = request.session['userID']
        wm = WebsiteManager(domain)
        return wm.joomlaInstall(request, userID)
    except KeyError:
        return redirect(loadLoginPage)

def installJoomla(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.installJoomla(userID, json.loads(request.body))
    except KeyError:
        return redirect(loadLoginPage)

def setupGit(request, domain):
    try:
        userID = request.session['userID']
        wm = WebsiteManager(domain)
        return wm.setupGit(request, userID)
    except KeyError:
        return redirect(loadLoginPage)

def setupGitRepo(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.setupGitRepo(userID, json.loads(request.body))
    except KeyError:
        return redirect(loadLoginPage)

def gitNotify(request, domain):
    try:
        wm = WebsiteManager(domain)
        return wm.gitNotify()
    except KeyError:
        return redirect(loadLoginPage)

def detachRepo(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.detachRepo(userID, json.loads(request.body))
    except KeyError:
        return redirect(loadLoginPage)

def changeBranch(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.changeBranch(userID, json.loads(request.body))
    except KeyError:
        return redirect(loadLoginPage)

def installPrestaShop(request, domain):
    try:
        userID = request.session['userID']
        wm = WebsiteManager(domain)
        return wm.installPrestaShop(request, userID)
    except KeyError:
        return redirect(loadLoginPage)

def prestaShopInstall(request):
    try:
        userID = request.session['userID']
        wm = WebsiteManager()
        return wm.prestaShopInstall(userID, json.loads(request.body))
    except KeyError:
        return redirect(loadLoginPage)
