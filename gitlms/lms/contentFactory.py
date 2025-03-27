from .models import Slide,Note,Video,temp_Note,temp_Slide,temp_Video
from .contentUploadStratagy import *


class ContentModelFactory:
    """
    Factory class to handle the creation of content models (Slide, Video, Note).
    The factory abstracts the logic for creating different content types.
    """
    @staticmethod
    def create_content_model(content_type, faculty, name, content_file):
        """
        This method creates and returns an instance of the appropriate content model 
        (Slide, Video, Note) based on the given content_type.

        Args:
            content_type (str): The type of content model to create ('slide', 'video', 'note').
            faculty (Faculty): The Faculty instance related to the content.
            name (str): The name of the content.
            content_file (File): The file associated with the content.

        Returns:
            object: The created content model instance (Slide, Video, or Note).
        """
        # Select the appropriate model class and strategy based on content_type
        if content_type == "slide":
            model_class = Slide
            upload_strategy = SlideUploadStrategy()
        elif content_type == "video":
            model_class = Video
            upload_strategy = VideoUploadStrategy()
        elif content_type == "note":
            model_class = Note
            upload_strategy = NoteUploadStrategy()
        else:
            raise ValueError("Invalid content type provided")

        # Create the model instance
        model_instance = model_class(
            name=name,
            faculty=faculty,
            content=content_file,
        )
        model_instance.content.upload_to = upload_strategy.get_upload_to  # Apply the upload strategy dynamically
        model_instance.save()  # Save the model instance to the database

        return model_instance


class TemporaryContentFactory:
    """
    Factory class to handle the creation of temporary content models (temp_Slide, temp_Video, temp_Note).
    The factory abstracts the logic for creating different temporary content types.
    """
    @staticmethod
    def create_temp_model(content_type, real_instance, faculty, name, content_file):
        """
        This method creates and returns an instance of the appropriate temporary content model 
        (temp_Slide, temp_Video, temp_Note) based on the given content_type.

        Args:
            content_type (str): The type of temporary content model to create ('temp_slide', 'temp_video', 'temp_note').
            real_instance (Slide/Video/Note): The real instance that the temporary model is related to.
            faculty (Faculty): The Faculty instance related to the content.
            name (str): The name of the content.
            content_file (File): The file associated with the content.

        Returns:
            object: The created temporary content model instance (temp_Slide, temp_Video, or temp_Note).
        """
        # Select the appropriate model class and strategy based on content_type
        if content_type == "temp_slide":
            model_class = temp_Slide
            upload_strategy = TempSlideUploadStrategy()
        elif content_type == "temp_video":
            model_class = temp_Video
            upload_strategy = TempVideoUploadStrategy()
        elif content_type == "temp_note":
            model_class = temp_Note
            upload_strategy = TempNoteUploadStrategy()
        else:
            raise ValueError("Invalid content type for temporary models provided")

        # Create the model instance
        model_instance = model_class(
            name=name,
            real=real_instance,  # Link to the real instance (Slide, Video, or Note)
            faculty=faculty,
            content=content_file,
        )
        model_instance.content.upload_to = upload_strategy.get_upload_to  # Apply the upload strategy dynamically
        model_instance.save()  # Save the model instance to the database

        return model_instance
