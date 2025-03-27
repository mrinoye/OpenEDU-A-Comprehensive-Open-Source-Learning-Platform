import os
from abc import ABC, abstractmethod

class UploadStrategy(ABC):
    """
    Abstract Strategy class that defines the upload behavior for file fields.
    """
    @abstractmethod
    def get_upload_to(self, instance, filename):
        pass



# Strategy for Slide model (Base)
class SlideUploadStrategy(UploadStrategy):
    def get_upload_to(self, instance, filename):
        return os.path.join(
            'contents',
            instance.faculty.course.department.name,
            instance.faculty.course.course_name,
            instance.faculty.name,
            'slides',  # Folder for regular slides
            filename
        )

# Strategy for Video model (Base)
class VideoUploadStrategy(UploadStrategy):
    def get_upload_to(self, instance, filename):
        return os.path.join(
            'contents',
            instance.faculty.course.department.name,
            instance.faculty.course.course_name,
            instance.faculty.name,
            'videos',  # Folder for regular videos
            filename
        )

# Strategy for Note model (Base)
class NoteUploadStrategy(UploadStrategy):
    def get_upload_to(self, instance, filename):
        return os.path.join(
            'contents',
            instance.faculty.course.department.name,
            instance.faculty.course.course_name,
            instance.faculty.name,
            'notes',  # Folder for regular notes
            filename
        )

# Strategy for Temporary Slide model
class TempSlideUploadStrategy(UploadStrategy):
    def get_upload_to(self, instance, filename):
        if hasattr(instance, 'real') and instance.real:
            return os.path.join(
                'contents',
                instance.real.faculty.course.department.name,
                instance.real.faculty.course.course_name,
                instance.real.faculty.name,
                'temp_slides',  # Temporary folder for slides
                filename
            )
        else:
            raise ValueError("Real instance is not linked properly for temp_Slide.")

# Strategy for Temporary Video model
class TempVideoUploadStrategy(UploadStrategy):
    def get_upload_to(self, instance, filename):
        if hasattr(instance, 'real') and instance.real:
            return os.path.join(
                'contents',
                instance.real.faculty.course.department.name,
                instance.real.faculty.course.course_name,
                instance.real.faculty.name,
                'temp_videos',  # Temporary folder for videos
                filename
            )
        else:
            raise ValueError("Real instance is not linked properly for temp_Video.")

# Strategy for Temporary Note model
class TempNoteUploadStrategy(UploadStrategy):
    def get_upload_to(self, instance, filename):
        if hasattr(instance, 'real') and instance.real:
            return os.path.join(
                'contents',
                instance.real.faculty.course.department.name,
                instance.real.faculty.course.course_name,
                instance.real.faculty.name,
                'temp_notes',  # Temporary folder for notes
                filename
            )
        else:
            raise ValueError("Real instance is not linked properly for temp_Note.")
