#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('latest')


from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'photon'  # from the Builder filename that created this script
expInfo = {'Participant ID': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
# expInfo['expName'] = expName
# expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s' % (expInfo['Participant ID'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/harmony/Dropbox/UCLA/SMT/textScreen.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
click = event.Mouse(win=win)
x, y = [None, None]
click.mouseClock = core.Clock()
text = visual.ImageStim(
    win=win,
    name='text', 
    image='/Users/harmony/Dropbox/UCLA/SMT/images/instructions.png', mask=None,
    ori=0, pos=(0, 0), size=(1.75, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
cross = visual.ImageStim(
    win=win,
    name='cross', 
    image='/Users/harmony/Dropbox/UCLA/SMT/images/cross.png', mask=None,
    ori=0, pos=(0, 0), size=(1.75, 1), #2 is too wide, and 1 is too thin
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
beep = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='beep')
beep.setVolume(1)

# Initialize components for Routine "trial"
trialClock = core.Clock()
test = visual.ImageStim(
    win=win,
    name='test', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
answer = keyboard.Keyboard()
background = visual.ImageStim(
    win=win,
    name='background', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "thank_you"
thank_youClock = core.Clock()
thanks = visual.TextStim(win=win, name='thanks',
    text='Thank you!',
    font='Arial',
    pos=(200, 200), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
# update component parameters for each repeat
# setup some python lists for storing info about the click
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructionsComponents = [click, text]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *click* updates
    if click.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        click.frameNStart = frameN  # exact frame index
        click.tStart = t  # local t and not account for scr refresh
        click.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(click, 'tStartRefresh')  # time at next scr refresh
        click.status = STARTED
        click.mouseClock.reset()
        prevButtonState = click.getPressed()  # if button is down already this ISN'T a new click
    if click.status == STARTED:  # only update if started and not finished!
        buttons = click.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # abort routine on response
                continueRoutine = False
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
x, y = click.getPos()
buttons = click.getPressed()
thisExp.addData('click.x', x)
thisExp.addData('click.y', y)
thisExp.addData('click.leftButton', buttons[0])
thisExp.addData('click.midButton', buttons[1])
thisExp.addData('click.rightButton', buttons[2])
thisExp.addData('click.started', click.tStart)
thisExp.addData('click.stopped', click.tStop)
thisExp.nextEntry()
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "fixation"-------
routineTimer.add(1.000000)
# update component parameters for each repeat
beep.setSound('A', secs=0.25, hamming=True)
beep.setVolume(1, log=False)
# keep track of which components have finished
fixationComponents = [cross, beep]
for thisComponent in fixationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "fixation"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixationClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *cross* updates
    if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cross.frameNStart = frameN  # exact frame index
        cross.tStart = t  # local t and not account for scr refresh
        cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
        cross.setAutoDraw(True)
    if cross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > cross.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            cross.tStop = t  # not accounting for scr refresh
            cross.frameNStop = frameN  # exact frame index
            win.timeOnFlip(cross, 'tStopRefresh')  # time at next scr refresh
            cross.setAutoDraw(False)
    # start/stop beep
    if beep.status == NOT_STARTED and t >= 0.75-frameTolerance:
        # keep track of start time/frame for later
        beep.frameNStart = frameN  # exact frame index
        beep.tStart = t  # local t and not account for scr refresh
        beep.tStartRefresh = tThisFlipGlobal  # on global time
        beep.play()  # start the sound (it finishes automatically)
    if beep.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > beep.tStartRefresh + 0.25-frameTolerance:
            # keep track of stop time/frame for later
            beep.tStop = t  # not accounting for scr refresh
            beep.frameNStop = frameN  # exact frame index
            win.timeOnFlip(beep, 'tStopRefresh')  # time at next scr refresh
            beep.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation"-------
for thisComponent in fixationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('cross.started', cross.tStartRefresh)
thisExp.addData('cross.stopped', cross.tStopRefresh)
beep.stop()  # ensure sound has stopped at end of routine
thisExp.addData('beep.started', beep.tStart)
thisExp.addData('beep.stopped', beep.tStop)

# ------Prepare to start Routine "trial"-------
# update component parameters for each repeat
answer.keys = []
answer.rt = []
# keep track of which components have finished
trialComponents = [test, answer, background]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial"-------
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *test* updates
    if test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        test.frameNStart = frameN  # exact frame index
        test.tStart = t  # local t and not account for scr refresh
        test.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test, 'tStartRefresh')  # time at next scr refresh
        test.setAutoDraw(True)
    
    # *answer* updates
    waitOnFlip = False
    if answer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        answer.frameNStart = frameN  # exact frame index
        answer.tStart = t  # local t and not account for scr refresh
        answer.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(answer, 'tStartRefresh')  # time at next scr refresh
        answer.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(answer.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(answer.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if answer.status == STARTED and not waitOnFlip:
        theseKeys = answer.getKeys(keyList=['left', 'right'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            answer.keys = theseKeys.name  # just the last key pressed
            answer.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # *background* updates
    if background.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        background.frameNStart = frameN  # exact frame index
        background.tStart = t  # local t and not account for scr refresh
        background.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(background, 'tStartRefresh')  # time at next scr refresh
        background.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('test.started', test.tStartRefresh)
thisExp.addData('test.stopped', test.tStopRefresh)
# check responses
if answer.keys in ['', [], None]:  # No response was made
    answer.keys = None
thisExp.addData('answer.keys',answer.keys)
if answer.keys != None:  # we had a response
    thisExp.addData('answer.rt', answer.rt)
thisExp.addData('answer.started', answer.tStartRefresh)
thisExp.addData('answer.stopped', answer.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('background.started', background.tStartRefresh)
thisExp.addData('background.stopped', background.tStopRefresh)
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "thank_you"-------
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
thank_youComponents = [thanks]
for thisComponent in thank_youComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thank_youClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "thank_you"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thank_youClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thank_youClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanks* updates
    if thanks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanks.frameNStart = frameN  # exact frame index
        thanks.tStart = t  # local t and not account for scr refresh
        thanks.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanks, 'tStartRefresh')  # time at next scr refresh
        thanks.setAutoDraw(True)
    if thanks.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thanks.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            thanks.tStop = t  # not accounting for scr refresh
            thanks.frameNStop = frameN  # exact frame index
            win.timeOnFlip(thanks, 'tStopRefresh')  # time at next scr refresh
            thanks.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thank_youComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thank_you"-------
for thisComponent in thank_youComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thanks.started', thanks.tStartRefresh)
thisExp.addData('thanks.stopped', thanks.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
