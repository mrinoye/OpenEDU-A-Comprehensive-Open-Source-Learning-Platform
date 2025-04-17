from .models import Slide, Video, Note, temp_Slide, temp_Video, temp_Note
from .contentUploadStratagy import SlideUploadStrategy, VideoUploadStrategy, NoteUploadStrategy, TempSlideUploadStrategy, TempVideoUploadStrategy, TempNoteUploadStrategy


from abc import ABC, abstractmethod

class AbstractContentFactory(ABC):
    
    @abstractmethod
    def create_content(self, faculty, name, content_file):
        pass


class SlideFactory(AbstractContentFactory):
    
    def create_content( faculty, name, content_file):
        # Create the Slide model instance
        slide_instance = Slide(
            name=name,
            faculty=faculty,
            content=content_file,
        )

        # Set the upload strategy
        upload_strategy = SlideUploadStrategy()
        slide_instance.content.upload_to = upload_strategy.get_upload_to

        # Save the Slide instance
        slide_instance.save()
        return slide_instance


class VideoFactory(AbstractContentFactory):
    
    def create_content( faculty, name, content_file):
        # Create the Video model instance
        video_instance = Video(
            name=name,
            faculty=faculty,
            content=content_file,
        )

        # Set the upload strategy
        upload_strategy = VideoUploadStrategy()
        video_instance.content.upload_to = upload_strategy.get_upload_to

        # Save the Video instance
        video_instance.save()
        return video_instance


class NoteFactory(AbstractContentFactory):
    
    def create_content(faculty, name, content_file):
        # Create the Note model instance
        note_instance = Note(
            name=name,
            faculty=faculty,
            content=content_file,
        )

        # Set the upload strategy
        upload_strategy = NoteUploadStrategy()
        note_instance.content.upload_to = upload_strategy.get_upload_to

        # Save the Note instance
        note_instance.save()
        return note_instance



class AbstractTemporaryContentFactory(ABC):

    @abstractmethod
    def create_temp_content( real_instance, faculty, name, content_file):
        pass


class TemporarySlideFactory(AbstractTemporaryContentFactory):
    
    def create_temp_content( real_instance, faculty, name, content_file):
        # Create the temp_Slide model instance
        temp_slide_instance = temp_Slide(
            name=name,
            real=real_instance,  # Link to the real Slide instance
            faculty=faculty,
            content=content_file,
        )

        # Set the upload strategy
        upload_strategy = TempSlideUploadStrategy()
        temp_slide_instance.content.upload_to = upload_strategy.get_upload_to

        # Save the temp_Slide instance
        temp_slide_instance.save()
        return temp_slide_instance


class TemporaryVideoFactory(AbstractTemporaryContentFactory):
    
    def create_temp_content( real_instance, faculty, name, content_file):
        # Create the temp_Video model instance
        temp_video_instance = temp_Video(
            name=name,
            real=real_instance,  # Link to the real Video instance
            faculty=faculty,
            content=content_file,
        )

        # Set the upload strategy
        upload_strategy = TempVideoUploadStrategy()
        temp_video_instance.content.upload_to = upload_strategy.get_upload_to

        # Save the temp_Video instance
        temp_video_instance.save()
        return temp_video_instance


class TemporaryNoteFactory(AbstractTemporaryContentFactory):
    
    def create_temp_content( real_instance, faculty, name, content_file):
        # Create the temp_Note model instance
        temp_note_instance = temp_Note(
            name=name,
            real=real_instance,  # Link to the real Note instance
            faculty=faculty,
            content=content_file,
        )

        # Set the upload strategy
        upload_strategy = TempNoteUploadStrategy()
        temp_note_instance.content.upload_to = upload_strategy.get_upload_to

        # Save the temp_Note instance
        temp_note_instance.save()
        return temp_note_instance
