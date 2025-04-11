from .models import Slide, Video, Note, temp_Slide, temp_Video, temp_Note
from .contentUploadStratagy import SlideUploadStrategy, VideoUploadStrategy, NoteUploadStrategy, TempSlideUploadStrategy, TempVideoUploadStrategy, TempNoteUploadStrategy


class SlideFactory:
    """
    Concrete Factory class to handle the creation of Slide model instances.
    """
    @staticmethod
    def create_slide(faculty, name, content_file):
        """
        Creates and returns an instance of the Slide model.

        Args:
            faculty (Faculty): The Faculty instance related to the content.
            name (str): The name of the content.
            content_file (File): The file associated with the content.

        Returns:
            Slide: The created Slide instance.
        """
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


class VideoFactory:
    """
    Concrete Factory class to handle the creation of Video model instances.
    """
    @staticmethod
    def create_video(faculty, name, content_file):
        """
        Creates and returns an instance of the Video model.

        Args:
            faculty (Faculty): The Faculty instance related to the content.
            name (str): The name of the content.
            content_file (File): The file associated with the content.

        Returns:
            Video: The created Video instance.
        """
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


class NoteFactory:
    """
    Concrete Factory class to handle the creation of Note model instances.
    """
    @staticmethod
    def create_note(faculty, name, content_file):
        """
        Creates and returns an instance of the Note model.

        Args:
            faculty (Faculty): The Faculty instance related to the content.
            name (str): The name of the content.
            content_file (File): The file associated with the content.

        Returns:
            Note: The created Note instance.
        """
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


class TemporarySlideFactory:
    """
    Concrete Factory class to handle the creation of temp_Slide model instances.
    """
    @staticmethod
    def create_temp_slide(real_instance, faculty, name, content_file):
        """
        Creates and returns an instance of the temp_Slide model.

        Args:
            real_instance (Slide): The real instance that the temporary slide is related to.
            faculty (Faculty): The Faculty instance related to the content.
            name (str): The name of the content.
            content_file (File): The file associated with the content.

        Returns:
            temp_Slide: The created temp_Slide instance.
        """
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


class TemporaryVideoFactory:
    """
    Concrete Factory class to handle the creation of temp_Video model instances.
    """
    @staticmethod
    def create_temp_video(real_instance, faculty, name, content_file):
        """
        Creates and returns an instance of the temp_Video model.

        Args:
            real_instance (Video): The real instance that the temporary video is related to.
            faculty (Faculty): The Faculty instance related to the content.
            name (str): The name of the content.
            content_file (File): The file associated with the content.

        Returns:
            temp_Video: The created temp_Video instance.
        """
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


class TemporaryNoteFactory:
    """
    Concrete Factory class to handle the creation of temp_Note model instances.
    """
    @staticmethod
    def create_temp_note(real_instance, faculty, name, content_file):
        """
        Creates and returns an instance of the temp_Note model.

        Args:
            real_instance (Note): The real instance that the temporary note is related to.
            faculty (Faculty): The Faculty instance related to the content.
            name (str): The name of the content.
            content_file (File): The file associated with the content.

        Returns:
            temp_Note: The created temp_Note instance.
        """
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
