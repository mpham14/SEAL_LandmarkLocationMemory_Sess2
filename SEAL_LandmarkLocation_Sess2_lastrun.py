#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Fri May 12 17:40:22 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'SEAL_LandmarkLocation_Sess2'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/mettapham/Downloads/SEAL_LandmarkLocationMemory_Sess2/SEAL_LandmarkLocation_Sess2_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Welcome" ---
text = visual.TextStim(win=win, name='text',
    text='Welcome to the SEAL Landmark Location Memory - Landmark Location Association Memory Task',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Instruction" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text='In this task, you will be presented with a map of the Kemper Museum and the following Landmarks. You are task with dragging the Landmarks to the correct location on the map. \n\nPress SPACEBAR to begin. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "trial" ---
image = visual.ImageStim(
    win=win,
    name='image', 
    image='Resources/Kemper Main.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.8, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
L1_shape = visual.Rect(
    win=win, name='L1_shape',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(-.09, -.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=0.0, depth=-1.0, interpolate=True)
L2_shape = visual.Rect(
    win=win, name='L2_shape',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(0.35, 0.20), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=0.0, depth=-2.0, interpolate=True)
L3_shape = visual.Rect(
    win=win, name='L3_shape',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(0.18, 0.3), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=0.0, depth=-3.0, interpolate=True)
L4_shape = visual.Rect(
    win=win, name='L4_shape',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(0.09, 0.27), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=0.0, depth=-4.0, interpolate=True)
L5_shape = visual.Rect(
    win=win, name='L5_shape',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(-.08, -.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=0.0, depth=-5.0, interpolate=True)
L6_shape = visual.Rect(
    win=win, name='L6_shape',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(-0.25, -.08), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=0.0, depth=-6.0, interpolate=True)
L7_shape = visual.Rect(
    win=win, name='L7_shape',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(0.1, 0.34), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=0.0, depth=-7.0, interpolate=True)
L8_shape = visual.Rect(
    win=win, name='L8_shape',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(0.3, 0.32), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=0.0, depth=-8.0, interpolate=True)
L9_shape = visual.Rect(
    win=win, name='L9_shape',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(0.19, 0.2), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=0.0, depth=-9.0, interpolate=True)
L10_shape = visual.Rect(
    win=win, name='L10_shape',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(-0.16, -0.05), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=0.0, depth=-10.0, interpolate=True)
L11_shape = visual.Rect(
    win=win, name='L11_shape',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(-0.01, 0.36), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=0.0, depth=-11.0, interpolate=True)
L12_shape = visual.Rect(
    win=win, name='L12_shape',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(0.21, 0.13), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=0.0, depth=-12.0, interpolate=True)
Instruction_text = visual.TextStim(win=win, name='Instruction_text',
    text='Click and drag each landmark to the correct location on the map. Even if you do not know the correct location, take your best guess.',
    font='Open Sans',
    pos=(0, 0.48), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-13.0);
key_resp_2 = keyboard.Keyboard()
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Press SPACEBAR when you are done to continue',
    font='Open Sans',
    pos=(0, -.47), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-16.0);
L1 = visual.ImageStim(
    win=win,
    name='L1', 
    image='Resources/Landmark_1.JPG', mask=None, anchor='center',
    ori=0.0, pos=(-0.7, 0.2), size=(0.085, 0.085),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-17.0)
L2 = visual.ImageStim(
    win=win,
    name='L2', 
    image='Resources/Landmark_2.JPG', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, 0.2), size=(0.085, 0.085),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-18.0)
L3 = visual.ImageStim(
    win=win,
    name='L3', 
    image='Resources/Landmark_3.jpg', mask=None, anchor='center',
    ori=0.0, pos=(-0.7, 0), size=(0.085, 0.085),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-19.0)
L4 = visual.ImageStim(
    win=win,
    name='L4', 
    image='Resources/Landmark_4.JPG', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, 0), size=(0.085, 0.085),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-20.0)
L5 = visual.ImageStim(
    win=win,
    name='L5', 
    image='Resources/Landmark_5.JPG', mask=None, anchor='center',
    ori=0.0, pos=(-0.7, -.2), size=(0.085, 0.085),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-21.0)
L6 = visual.ImageStim(
    win=win,
    name='L6', 
    image='Resources/Landmark_6.JPG', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, -.2), size=(0.085, 0.085),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-22.0)
L7 = visual.ImageStim(
    win=win,
    name='L7', 
    image='Resources/Landmark_7.JPG', mask=None, anchor='center',
    ori=0.0, pos=(0.5, 0.2), size=(0.085, 0.085),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-23.0)
L8 = visual.ImageStim(
    win=win,
    name='L8', 
    image='Resources/Landmark_8.JPG', mask=None, anchor='center',
    ori=0.0, pos=(0.7, 0.2), size=(0.085, 0.085),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-24.0)
L9 = visual.ImageStim(
    win=win,
    name='L9', 
    image='Resources/Landmark_9.JPG', mask=None, anchor='center',
    ori=0.0, pos=(0.5, 0), size=(0.085, 0.085),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-25.0)
L10 = visual.ImageStim(
    win=win,
    name='L10', 
    image='Resources/Landmark_10.JPG', mask=None, anchor='center',
    ori=0.0, pos=(0.7, 0), size=(0.085, 0.085),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-26.0)
L11 = visual.ImageStim(
    win=win,
    name='L11', 
    image='Resources/Landmark_11.JPG', mask=None, anchor='center',
    ori=0.0, pos=(0.5, -0.2), size=(0.085, 0.085),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-27.0)
L12 = visual.ImageStim(
    win=win,
    name='L12', 
    image='Resources/Landmark_12.JPG', mask=None, anchor='center',
    ori=0.0, pos=(0.7, -0.2), size=(0.085, 0.085),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-28.0)
# Run 'Begin Experiment' code from code
L1_opacity = 0.5
L2_opacity = 0.5
L3_opacity = 0.5
L4_opacity = 0.5
L5_opacity = 0.5
L6_opacity = 0.5
L7_opacity = 0.5
L8_opacity = 0.5
L9_opacity = 0.5
L10_opacity = 0.5
L11_opacity = 0.5
L12_opacity = 0.5

def movePicked(picked, mouse, grabbed):
    if grabbed is not None and mouse.isPressedIn(grabbed):
        grabbed.pos = mouse.getPos()
        return grabbed
    else:
        for piece in picked:
            if mouse.isPressedIn(piece) and grabbed is None:
                return piece

# --- Initialize components for Routine "End" ---

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Welcome" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
WelcomeComponents = [text]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Welcome" ---
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.stopped')
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Welcome" ---
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# --- Prepare to start Routine "Instruction" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
InstructionComponents = [text_2, key_resp]
for thisComponent in InstructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instruction" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_2.started')
        text_2.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instruction" ---
for thisComponent in InstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "trial" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# setup some python lists for storing info about the mouse
mouse.x = []
mouse.y = []
mouse.leftButton = []
mouse.midButton = []
mouse.rightButton = []
mouse.time = []
gotValidClick = False  # until a click is received
# Run 'Begin Routine' code from code
picked = []
movingPiece = None

pieces = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12]

score = 0
# keep track of which components have finished
trialComponents = [image, L1_shape, L2_shape, L3_shape, L4_shape, L5_shape, L6_shape, L7_shape, L8_shape, L9_shape, L10_shape, L11_shape, L12_shape, Instruction_text, key_resp_2, mouse, text_3, L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12]
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
frameN = -1

# --- Run Routine "trial" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image.started')
        image.setAutoDraw(True)
    
    # *L1_shape* updates
    if L1_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        L1_shape.frameNStart = frameN  # exact frame index
        L1_shape.tStart = t  # local t and not account for scr refresh
        L1_shape.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L1_shape, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L1_shape.started')
        L1_shape.setAutoDraw(True)
    
    # *L2_shape* updates
    if L2_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        L2_shape.frameNStart = frameN  # exact frame index
        L2_shape.tStart = t  # local t and not account for scr refresh
        L2_shape.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L2_shape, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L2_shape.started')
        L2_shape.setAutoDraw(True)
    
    # *L3_shape* updates
    if L3_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        L3_shape.frameNStart = frameN  # exact frame index
        L3_shape.tStart = t  # local t and not account for scr refresh
        L3_shape.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L3_shape, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L3_shape.started')
        L3_shape.setAutoDraw(True)
    
    # *L4_shape* updates
    if L4_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        L4_shape.frameNStart = frameN  # exact frame index
        L4_shape.tStart = t  # local t and not account for scr refresh
        L4_shape.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L4_shape, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L4_shape.started')
        L4_shape.setAutoDraw(True)
    
    # *L5_shape* updates
    if L5_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        L5_shape.frameNStart = frameN  # exact frame index
        L5_shape.tStart = t  # local t and not account for scr refresh
        L5_shape.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L5_shape, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L5_shape.started')
        L5_shape.setAutoDraw(True)
    
    # *L6_shape* updates
    if L6_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        L6_shape.frameNStart = frameN  # exact frame index
        L6_shape.tStart = t  # local t and not account for scr refresh
        L6_shape.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L6_shape, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L6_shape.started')
        L6_shape.setAutoDraw(True)
    
    # *L7_shape* updates
    if L7_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        L7_shape.frameNStart = frameN  # exact frame index
        L7_shape.tStart = t  # local t and not account for scr refresh
        L7_shape.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L7_shape, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L7_shape.started')
        L7_shape.setAutoDraw(True)
    
    # *L8_shape* updates
    if L8_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        L8_shape.frameNStart = frameN  # exact frame index
        L8_shape.tStart = t  # local t and not account for scr refresh
        L8_shape.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L8_shape, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L8_shape.started')
        L8_shape.setAutoDraw(True)
    
    # *L9_shape* updates
    if L9_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        L9_shape.frameNStart = frameN  # exact frame index
        L9_shape.tStart = t  # local t and not account for scr refresh
        L9_shape.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L9_shape, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L9_shape.started')
        L9_shape.setAutoDraw(True)
    
    # *L10_shape* updates
    if L10_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        L10_shape.frameNStart = frameN  # exact frame index
        L10_shape.tStart = t  # local t and not account for scr refresh
        L10_shape.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L10_shape, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L10_shape.started')
        L10_shape.setAutoDraw(True)
    
    # *L11_shape* updates
    if L11_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        L11_shape.frameNStart = frameN  # exact frame index
        L11_shape.tStart = t  # local t and not account for scr refresh
        L11_shape.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L11_shape, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L11_shape.started')
        L11_shape.setAutoDraw(True)
    
    # *L12_shape* updates
    if L12_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        L12_shape.frameNStart = frameN  # exact frame index
        L12_shape.tStart = t  # local t and not account for scr refresh
        L12_shape.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L12_shape, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L12_shape.started')
        L12_shape.setAutoDraw(True)
    
    # *Instruction_text* updates
    if Instruction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instruction_text.frameNStart = frameN  # exact frame index
        Instruction_text.tStart = t  # local t and not account for scr refresh
        Instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instruction_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Instruction_text.started')
        Instruction_text.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_2.started')
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # *mouse* updates
    if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mouse.started', t)
        mouse.status = STARTED
        mouse.mouseClock.reset()
        prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                x, y = mouse.getPos()
                mouse.x.append(x)
                mouse.y.append(y)
                buttons = mouse.getPressed()
                mouse.leftButton.append(buttons[0])
                mouse.midButton.append(buttons[1])
                mouse.rightButton.append(buttons[2])
                mouse.time.append(mouse.mouseClock.getTime())
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_3.started')
        text_3.setAutoDraw(True)
    
    # *L1* updates
    if L1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        L1.frameNStart = frameN  # exact frame index
        L1.tStart = t  # local t and not account for scr refresh
        L1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L1.started')
        L1.setAutoDraw(True)
    
    # *L2* updates
    if L2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        L2.frameNStart = frameN  # exact frame index
        L2.tStart = t  # local t and not account for scr refresh
        L2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L2.started')
        L2.setAutoDraw(True)
    
    # *L3* updates
    if L3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        L3.frameNStart = frameN  # exact frame index
        L3.tStart = t  # local t and not account for scr refresh
        L3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L3.started')
        L3.setAutoDraw(True)
    
    # *L4* updates
    if L4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        L4.frameNStart = frameN  # exact frame index
        L4.tStart = t  # local t and not account for scr refresh
        L4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L4.started')
        L4.setAutoDraw(True)
    
    # *L5* updates
    if L5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        L5.frameNStart = frameN  # exact frame index
        L5.tStart = t  # local t and not account for scr refresh
        L5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L5.started')
        L5.setAutoDraw(True)
    
    # *L6* updates
    if L6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        L6.frameNStart = frameN  # exact frame index
        L6.tStart = t  # local t and not account for scr refresh
        L6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L6.started')
        L6.setAutoDraw(True)
    
    # *L7* updates
    if L7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        L7.frameNStart = frameN  # exact frame index
        L7.tStart = t  # local t and not account for scr refresh
        L7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L7.started')
        L7.setAutoDraw(True)
    
    # *L8* updates
    if L8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        L8.frameNStart = frameN  # exact frame index
        L8.tStart = t  # local t and not account for scr refresh
        L8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L8.started')
        L8.setAutoDraw(True)
    
    # *L9* updates
    if L9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        L9.frameNStart = frameN  # exact frame index
        L9.tStart = t  # local t and not account for scr refresh
        L9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L9, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L9.started')
        L9.setAutoDraw(True)
    
    # *L10* updates
    if L10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        L10.frameNStart = frameN  # exact frame index
        L10.tStart = t  # local t and not account for scr refresh
        L10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L10, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L10.started')
        L10.setAutoDraw(True)
    
    # *L11* updates
    if L11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        L11.frameNStart = frameN  # exact frame index
        L11.tStart = t  # local t and not account for scr refresh
        L11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L11, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L11.started')
        L11.setAutoDraw(True)
    
    # *L12* updates
    if L12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        L12.frameNStart = frameN  # exact frame index
        L12.tStart = t  # local t and not account for scr refresh
        L12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L12, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L12.started')
        L12.setAutoDraw(True)
    # Run 'Each Frame' code from code
    for piece in pieces:
        if mouse.isPressedIn(piece) and movingPiece is None:
            picked.append(piece)
            
    movingPiece = movePicked(picked, mouse, movingPiece)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "trial" ---
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse.x', mouse.x)
thisExp.addData('mouse.y', mouse.y)
thisExp.addData('mouse.leftButton', mouse.leftButton)
thisExp.addData('mouse.midButton', mouse.midButton)
thisExp.addData('mouse.rightButton', mouse.rightButton)
thisExp.addData('mouse.time', mouse.time)
thisExp.nextEntry()
# Run 'End Routine' code from code
L1FinalLoc = L1.pos
L2FinalLoc = L2.pos
L3FinalLoc = L3.pos
L4FinalLoc = L4.pos
L5FinalLoc = L5.pos
L6FinalLoc = L6.pos
L7FinalLoc = L7.pos
L8FinalLoc = L8.pos
L9FinalLoc = L9.pos
L10FinalLoc = L10.pos
L11FinalLoc = L11.pos
L12FinalLoc = L12.pos

if L1_shape.contains(L1FinalLoc):
    L1_corr = 2
    L1_opacity = 1
    score += 2
elif L1_shape.contains(L2FinalLoc):
    L1_corr = 1
    score += 1
elif L1_shape.contains(L3FinalLoc):
    L1_corr = 1
    score += 1
elif L1_shape.contains(L4FinalLoc):
    L1_corr = 1
    score += 1
elif L1_shape.contains(L5FinalLoc):
    L1_corr = 1
    score += 1
elif L1_shape.contains(L6FinalLoc):
    L1_corr = 1
    score += 1
elif L1_shape.contains(L7FinalLoc):
    L1_corr = 1
    score += 1
elif L1_shape.contains(L8FinalLoc):
    L1_corr = 1
    score += 1
elif L1_shape.contains(L9FinalLoc):
    L1_corr = 1
    score += 1
elif L1_shape.contains(L10FinalLoc):
    L1_corr = 1
    score += 1
elif L1_shape.contains(L11FinalLoc):
    L1_corr = 1
    score += 1
elif L1_shape.contains(L12FinalLoc):
    L1_corr = 1
    score += 1
else:
    L1_corr = 0 
    L1_opacity = 0
    
thisExp.addData('L1_loc', L1FinalLoc)
thisExp.addData('L1_corr', L1_corr)

if L2_shape.contains(L2FinalLoc):
    L2_corr = 2
    L2_opacity = 1
    score += 2
elif L2_shape.contains(L1FinalLoc):
    L2_corr = 1
    score += 1
elif L2_shape.contains(L3FinalLoc):
    L2_corr = 1
    score += 1
elif L2_shape.contains(L4FinalLoc):
    L2_corr = 1
    score += 1
elif L2_shape.contains(L5FinalLoc):
    L2_corr = 1
    score += 1
elif L2_shape.contains(L6FinalLoc):
    L2_corr = 1
    score += 1
elif L2_shape.contains(L7FinalLoc):
    L2_corr = 1
    score += 1
elif L2_shape.contains(L8FinalLoc):
    L2_corr = 1
    score += 1
elif L2_shape.contains(L9FinalLoc):
    L2_corr = 1
    score += 1
elif L2_shape.contains(L10FinalLoc):
    L2_corr = 1
    score += 1
elif L2_shape.contains(L11FinalLoc):
    L2_corr = 1
    score += 1
elif L2_shape.contains(L12FinalLoc):
    L2_corr = 1
    score += 1
else:
    L2_corr = 0 
    L2_opacity = 0
    
thisExp.addData('L2_loc', L2FinalLoc)
thisExp.addData('L2_corr', L2_corr)

if L3_shape.contains(L3FinalLoc):
    L3_corr = 2
    L3_opacity = 1
    score += 2
elif L3_shape.contains(L1FinalLoc):
    L3_corr = 1
    score += 1
elif L3_shape.contains(L2FinalLoc):
    L3_corr = 1
    score += 1
elif L3_shape.contains(L4FinalLoc):
    L3_corr = 1
    score += 1
elif L3_shape.contains(L5FinalLoc):
    L3_corr = 1
    score += 1
elif L3_shape.contains(L6FinalLoc):
    L3_corr = 1
    score += 1
elif L1_shape.contains(L7FinalLoc):
    L1_corr = 1
    score += 1
elif L3_shape.contains(L8FinalLoc):
    L3_corr = 1
    score += 1
elif L3_shape.contains(L9FinalLoc):
    L3_corr = 1
    score += 1
elif L3_shape.contains(L10FinalLoc):
    L3_corr = 1
    score += 1
elif L3_shape.contains(L11FinalLoc):
    L3_corr = 1
    score += 1
elif L3_shape.contains(L12FinalLoc):
    L3_corr = 1
    score += 1
else:
    L3_corr = 0 
    L3_opacity = 0
    
thisExp.addData('L3_loc', L3FinalLoc)
thisExp.addData('L3_corr', L3_corr)

if L4_shape.contains(L4FinalLoc):
    L4_corr = 2
    L4_opacity = 1
    score += 2
elif L4_shape.contains(L2FinalLoc):
    L4_corr = 1
    score += 1
elif L4_shape.contains(L3FinalLoc):
    L4_corr = 1
    score += 1
elif L4_shape.contains(L1FinalLoc):
    L4_corr = 1
    score += 1
elif L4_shape.contains(L5FinalLoc):
    L4_corr = 1
    score += 1
elif L4_shape.contains(L6FinalLoc):
    L4_corr = 1
    score += 1
elif L4_shape.contains(L7FinalLoc):
    L4_corr = 1
    score += 1
elif L4_shape.contains(L8FinalLoc):
    L4_corr = 1
    score += 1
elif L4_shape.contains(L9FinalLoc):
    L4_corr = 1
    score += 1
elif L4_shape.contains(L10FinalLoc):
    L4_corr = 1
    score += 1
elif L4_shape.contains(L11FinalLoc):
    L4_corr = 1
    score += 1
elif L4_shape.contains(L12FinalLoc):
    L4_corr = 1
    score += 1
else:
    L4_corr = 0 
    L4_opacity = 0
    
thisExp.addData('L4_loc', L4FinalLoc)
thisExp.addData('L4_corr', L4_corr)

if L5_shape.contains(L5FinalLoc):
    L5_corr = 2
    L5_opacity = 1
    score += 2
elif L5_shape.contains(L2FinalLoc):
    L5_corr = 1
    score += 1
elif L5_shape.contains(L3FinalLoc):
    L5_corr = 1
    score += 1
elif L5_shape.contains(L4FinalLoc):
    L5_corr = 1
    score += 1
elif L5_shape.contains(L1FinalLoc):
    L5_corr = 1
    score += 1
elif L5_shape.contains(L6FinalLoc):
    L5_corr = 1
    score += 1
elif L5_shape.contains(L7FinalLoc):
    L5_corr = 1
    score += 1
elif L5_shape.contains(L8FinalLoc):
    L5_corr = 1
    score += 1
elif L5_shape.contains(L9FinalLoc):
    L5_corr = 1
    score += 1
elif L5_shape.contains(L10FinalLoc):
    L5_corr = 1
    score += 1
elif L5_shape.contains(L11FinalLoc):
    L5_corr = 1
    score += 1
elif L5_shape.contains(L12FinalLoc):
    L5_corr = 1
    score += 1
else:
    L5_corr = 0 
    L5_opacity = 0
    
thisExp.addData('L5_loc', L5FinalLoc)
thisExp.addData('L5_corr', L5_corr)

if L6_shape.contains(L6FinalLoc):
    L6_corr = 2
    L6_opacity = 1
    score += 2
elif L6_shape.contains(L2FinalLoc):
    L6_corr = 1
    score += 1
elif L6_shape.contains(L3FinalLoc):
    L6_corr = 1
    score += 1
elif L6_shape.contains(L4FinalLoc):
    L6_corr = 1
    score += 1
elif L6_shape.contains(L5FinalLoc):
    L6_corr = 1
    score += 1
elif L6_shape.contains(L1FinalLoc):
    L6_corr = 1
    score += 1
elif L6_shape.contains(L7FinalLoc):
    L6_corr = 1
    score += 1
elif L6_shape.contains(L8FinalLoc):
    L6_corr = 1
    score += 1
elif L1_shape.contains(L9FinalLoc):
    L1_corr = 1
    score += 1
elif L6_shape.contains(L10FinalLoc):
    L6_corr = 1
    score += 1
elif L6_shape.contains(L11FinalLoc):
    L6_corr = 1
    score += 1
elif L6_shape.contains(L12FinalLoc):
    L6_corr = 1
    score += 1
else:
    L6_corr = 0 
    L6_opacity = 0
    
thisExp.addData('L6_loc', L6FinalLoc)
thisExp.addData('L6_corr', L6_corr)

if L7_shape.contains(L7FinalLoc):
    L7_corr = 2
    L7_opacity = 1
    score += 2
elif L7_shape.contains(L2FinalLoc):
    L7_corr = 1
    score += 1
elif L7_shape.contains(L3FinalLoc):
    L7_corr = 1
    score += 1
elif L7_shape.contains(L4FinalLoc):
    L7_corr = 1
    score += 1
elif L7_shape.contains(L5FinalLoc):
    L7_corr = 1
    score += 1
elif L7_shape.contains(L6FinalLoc):
    L7_corr = 1
    score += 1
elif L7_shape.contains(L1FinalLoc):
    L7_corr = 1
    score += 1
elif L7_shape.contains(L8FinalLoc):
    L7_corr = 1
    score += 1
elif L7_shape.contains(L9FinalLoc):
    L7_corr = 1
    score += 1
elif L7_shape.contains(L10FinalLoc):
    L7_corr = 1
    score += 1
elif L7_shape.contains(L11FinalLoc):
    L7_corr = 1
    score += 1
elif L7_shape.contains(L12FinalLoc):
    L7_corr = 1
    score += 1
else:
    L7_corr = 0 
    L7_opacity = 0
    
thisExp.addData('L7_loc', L7FinalLoc)
thisExp.addData('L7_corr', L7_corr)

if L8_shape.contains(L8FinalLoc):
    L8_corr = 2
    L8_opacity = 1
    score += 2
elif L8_shape.contains(L2FinalLoc):
    L8_corr = 1
    score += 1
elif L8_shape.contains(L3FinalLoc):
    L8_corr = 1
    score += 1
elif L8_shape.contains(L4FinalLoc):
    L8_corr = 1
    score += 1
elif L8_shape.contains(L5FinalLoc):
    L8_corr = 1
    score += 1
elif L8_shape.contains(L6FinalLoc):
    L8_corr = 1
    score += 1
elif L8_shape.contains(L7FinalLoc):
    L8_corr = 1
    score += 1
elif L8_shape.contains(L1FinalLoc):
    L8_corr = 1
    score += 1
elif L8_shape.contains(L9FinalLoc):
    L8_corr = 1
    score += 1
elif L8_shape.contains(L10FinalLoc):
    L8_corr = 1
    score += 1
elif L8_shape.contains(L11FinalLoc):
    L8_corr = 1
    score += 1
elif L8_shape.contains(L12FinalLoc):
    L8_corr = 1
    score += 1
else:
    L8_corr = 0 
    L8_opacity = 0
    
thisExp.addData('L8_loc', L8FinalLoc)
thisExp.addData('L8_corr', L8_corr)

if L9_shape.contains(L9FinalLoc):
    L9_corr = 2
    L9_opacity = 1
    score += 2
elif L9_shape.contains(L2FinalLoc):
    L9_corr = 1
    score += 1
elif L9_shape.contains(L3FinalLoc):
    L9_corr = 1
    score += 1
elif L9_shape.contains(L4FinalLoc):
    L9_corr = 1
    score += 1
elif L9_shape.contains(L5FinalLoc):
    L9_corr = 1
    score += 1
elif L9_shape.contains(L6FinalLoc):
    L9_corr = 1
    score += 1
elif L9_shape.contains(L7FinalLoc):
    L9_corr = 1
    score += 1
elif L9_shape.contains(L8FinalLoc):
    L9_corr = 1
    score += 1
elif L9_shape.contains(L1FinalLoc):
    L9_corr = 1
    score += 1
elif L9_shape.contains(L10FinalLoc):
    L9_corr = 1
    score += 1
elif L9_shape.contains(L11FinalLoc):
    L9_corr = 1
    score += 1
elif L9_shape.contains(L12FinalLoc):
    L9_corr = 1
    score += 1
else:
    L9_corr = 0 
    L9_opacity = 0
    
thisExp.addData('L9_loc', L9FinalLoc)
thisExp.addData('L9_corr', L9_corr)

if L10_shape.contains(L10FinalLoc):
    L10_corr = 2
    L10_opacity = 1
    score += 2
elif L10_shape.contains(L2FinalLoc):
    L10_corr = 1
    score += 1
elif L10_shape.contains(L3FinalLoc):
    L10_corr = 1
    score += 1
elif L10_shape.contains(L4FinalLoc):
    L10_corr = 1
    score += 1
elif L10_shape.contains(L5FinalLoc):
    L10_corr = 1
    score += 1
elif L10_shape.contains(L6FinalLoc):
    L10_corr = 1
    score += 1
elif L10_shape.contains(L7FinalLoc):
    L10_corr = 1
    score += 1
elif L10_shape.contains(L8FinalLoc):
    L10_corr = 1
    score += 1
elif L10_shape.contains(L9FinalLoc):
    L10_corr = 1
    score += 1
elif L10_shape.contains(L1FinalLoc):
    L10_corr = 1
    score += 1
elif L10_shape.contains(L11FinalLoc):
    L10_corr = 1
    score += 1
elif L10_shape.contains(L12FinalLoc):
    L10_corr = 1
    score += 1
else:
    L10_corr = 0 
    L10_opacity = 0
    
thisExp.addData('L10_loc', L10FinalLoc)
thisExp.addData('L10_corr', L10_corr)

if L11_shape.contains(L11FinalLoc):
    L11_corr = 2
    L11_opacity = 1
    score += 2
elif L11_shape.contains(L2FinalLoc):
    L11_corr = 1
    score += 1
elif L11_shape.contains(L3FinalLoc):
    L11_corr = 1
    score += 1
elif L11_shape.contains(L4FinalLoc):
    L11_corr = 1
    score += 1
elif L11_shape.contains(L5FinalLoc):
    L11_corr = 1
    score += 1
elif L11_shape.contains(L6FinalLoc):
    L11_corr = 1
    score += 1
elif L11_shape.contains(L7FinalLoc):
    L11_corr = 1
    score += 1
elif L11_shape.contains(L8FinalLoc):
    L11_corr = 1
    score += 1
elif L11_shape.contains(L9FinalLoc):
    L1_corr = 1
    score += 1
elif L11_shape.contains(L10FinalLoc):
    L11_corr = 1
    score += 1
elif L11_shape.contains(L1FinalLoc):
    L11_corr = 1
    score += 1
elif L11_shape.contains(L12FinalLoc):
    L11_corr = 1
    score += 1
else:
    L11_corr = 0 
    L11_opacity = 0
    
thisExp.addData('L11_loc', L11FinalLoc)
thisExp.addData('L11_corr', L11_corr)

if L12_shape.contains(L12FinalLoc):
    L12_corr = 2
    L12_opacity = 1
    score += 2
elif L12_shape.contains(L2FinalLoc):
    L12_corr = 1
    score += 1
elif L12_shape.contains(L3FinalLoc):
    L12_corr = 1
    score += 1
elif L12_shape.contains(L4FinalLoc):
    L12_corr = 1
    score += 1
elif L12_shape.contains(L5FinalLoc):
    L12_corr = 1
    score += 1
elif L12_shape.contains(L6FinalLoc):
    L12_corr = 1
    score += 1
elif L12_shape.contains(L7FinalLoc):
    L12_corr = 1
    score += 1
elif L12_shape.contains(L8FinalLoc):
    L12_corr = 1
    score += 1
elif L12_shape.contains(L9FinalLoc):
    L12_corr = 1
    score += 1
elif L12_shape.contains(L10FinalLoc):
    L12_corr = 1
    score += 1
elif L12_shape.contains(L11FinalLoc):
    L12_corr = 1
    score += 1
elif L12_shape.contains(L1FinalLoc):
    L12_corr = 1
    score += 1
else:
    L12_corr = 0 
    L12_opacity = 0
    
thisExp.addData('L12_loc', L12FinalLoc)
thisExp.addData('L12_corr', L12_corr)
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "End" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = []
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "End" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "End" ---
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
