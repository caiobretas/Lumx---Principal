from controllers.controllerGoogle.controllerGoogleGmail import GoogleGmail
import base64
import os

messageId = '1884e330c373ec2d'
attachmentId = 'ANGjdJ9ecABXisJcZb166H9Z7-kA-lvWLVZbApOTUkdfRi7MJs0AYtyQ7H7cKtta2ErcPKPJEVlSV65R3mCavXx2epbfTlHl-Q4Mn0p7Nl2_bi9leq10yEzAWaw2wIPoWHPhYt11P2W6boG06tXTUsMjmMc5hhz5u8oZ8OmIQy-65-gOIsWEHXrU41SWNPPAIhm6FYU1-UyJSuI1GNVOW2gUwJG2LMBoGPa2LqcGB5GiHACrM4gbll2_fHou3tEQBeXIUcC1YchO238jobc2DK2WgWDeNSeKqeLZ5FMLhYOFcHifCmLDs48tDYSVr9olCcIHG-kByLRnEEXOTVL83QAfaYI89Gc71dpOXk_5b4oxtKDxbfSXUkqTARaapcZ-V7IIp0SOCh1N0gPYL1cM'
attachment: dict = GoogleGmail().getAttachmentById(messageId,attachmentId)

data_encoded = attachment.get('data', None)
data_binary = base64.urlsafe_b64decode(data_encoded)

from controllers.controllerGoogle.controllerGoogleDrive import GoogleDrive

# GoogleDrive().createFolder('teste', parentId='1jWV8_GnkrvS9aMmWRCLbt9pOqj6ei8ui ')
GoogleDrive().getSharedDrives()
# GoogleDrive().deleteSharedDrives('0APWHM2MD0pXDUk9PVA')