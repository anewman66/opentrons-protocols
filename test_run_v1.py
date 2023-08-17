from opentrons import protocol_api

# 5 major parts: Metadata and version selection, run function,
# labware, pipettes and commands.

#metadata
metadata = {
    'protocolName': 'Test Protocol 1'
    'author': 'Alex Newman <a.newman@tees.ac.uk>'
    'description': 'This will do some basic movements.'
    'apiLevel': '2.9'
    }

# Protocol run function

def run(protocol: protocol_api.ProtocolContext):
    # labware (plates, tips, etc.) Coordinates with existing library of labware
    plate= protocol.load_labware('corning_96_wellplate_360ul_flat',1)
    tiprack= protocol.load_labware('opentrons_96_tiprack_300ul',2)
    # pipettes (list all pipettes currently installed.)
    left_pipette = protocol.load_intstrument('p300_single',
                                             'left',
                                             tip_racks=[tiprack])
    
    # commands
    left.pipette.pick_up_tip()
    left_pipette.aspirate(100, plate['A1'])
    left_pipette.dispense(10, plate['B1'])
    left_pipette.dispense(20, plate['B2'])
    left_pipette.dispense(30, plate['B3'])
    left_pipette.dispense(20, plate['B4'])
    left_pipette.dispense(20, plate['B5'])
    left_pipette.drop_tip()

    

    
