import random
from AttachmentEnums import (
    Muzzles, 
    Barrels, 
    Arms, 
    Lasers, 
    Optics, 
    Stocks, 
    Combs, 
    Guards, 
    Bolts, 
    Levers, 
    RearGrips, 
    TriggerActions, 
    Magazines, 
    Loaders, 
    Wires, 
    Rails, 
    AmmoTypes, 
    Underbarrels, 
    CarryHandles
)

class AttachmentSuggestion:
    @staticmethod
    def suggest_attachments():
        attachment_types = [
            Muzzles, 
            Barrels, 
            Arms, 
            Lasers, 
            Optics, 
            Stocks, 
            Combs, 
            Guards, 
            Bolts, 
            Levers, 
            RearGrips, 
            TriggerActions, 
            Magazines, 
            Loaders, 
            Wires, 
            Rails, 
            AmmoTypes, 
            Underbarrels, 
            CarryHandles
        ]
        num_attachment_types = random.randint(3, 5)
        selected_attachment_types = random.sample(attachment_types, num_attachment_types)
        selected_attachments = {}
        for attachment_type in selected_attachment_types:
            attachment = random.choice(list(attachment_type))
            selected_attachments[attachment_type.__name__] = attachment.value
        return selected_attachments

# Example usage:
attachments = AttachmentSuggestion.suggest_attachments()
for attachment_type, attachment in attachments.items():
    attachments