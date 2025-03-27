# This file contains the Adapter class that chooses the appropriate upload strategy for each content type.
# The Adapter class is used in the models.py file to set the upload path for the FileField based on the content type.

import os
from .contentUploadStratagy import SlideUploadStrategy, VideoUploadStrategy, NoteUploadStrategy, TempSlideUploadStrategy, TempVideoUploadStrategy, TempNoteUploadStrategy

class ContentUploadAdapter:
    """
    The Adapter class that chooses the appropriate upload strategy for each content type.
    """
    def __init__(self, content_type, is_temp=False):
        self.content_type = content_type
        self.is_temp = is_temp

    def get_upload_strategy(self):
        """
        Returns the appropriate upload strategy based on the content type and whether it's temporary.
        """
        if self.is_temp:
            if self.content_type == 'slide':
                return TempSlideUploadStrategy()
            elif self.content_type == 'video':
                return TempVideoUploadStrategy()
            elif self.content_type == 'note':
                return TempNoteUploadStrategy()
        else:
            if self.content_type == 'slide':
                return SlideUploadStrategy()
            elif self.content_type == 'video':
                return VideoUploadStrategy()
            elif self.content_type == 'note':
                return NoteUploadStrategy()

        raise ValueError(f"Unsupported content type: {self.content_type}")
