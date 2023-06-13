from controllers.controllerGoogle.controllerGoogleGmail import GoogleGmail
from controllers.controllerGoogle.controllerGoogleDrive import GoogleDrive
from controllers.controllerPipeDrive.controllerPipeDrive import ControllerPipeDrive
import base64
import os

controllerDrive = GoogleDrive()
controllerGmail = GoogleGmail()
controllerPipe = ControllerPipeDrive()

# messageId = '1884e330c373ec2d'
# attachmentId = 'ANGjdJ9ecABXisJcZb166H9Z7-kA-lvWLVZbApOTUkdfRi7MJs0AYtyQ7H7cKtta2ErcPKPJEVlSV65R3mCavXx2epbfTlHl-Q4Mn0p7Nl2_bi9leq10yEzAWaw2wIPoWHPhYt11P2W6boG06tXTUsMjmMc5hhz5u8oZ8OmIQy-65-gOIsWEHXrU41SWNPPAIhm6FYU1-UyJSuI1GNVOW2gUwJG2LMBoGPa2LqcGB5GiHACrM4gbll2_fHou3tEQBeXIUcC1YchO238jobc2DK2WgWDeNSeKqeLZ5FMLhYOFcHifCmLDs48tDYSVr9olCcIHG-kByLRnEEXOTVL83QAfaYI89Gc71dpOXk_5b4oxtKDxbfSXUkqTARaapcZ-V7IIp0SOCh1N0gPYL1cM'

# attachment: dict = controllerGmail.getAttachmentById(messageId,attachmentId)

# controllerDrive.uploadFile(attachment, 'Teste', '1JS8MCpBsNR-jp1APrxq7wR9Be2X7o1bd')